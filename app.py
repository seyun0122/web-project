import os
from pathlib import Path

import gradio as gr
import torch

from PIL import Image
from torchvision import transforms

from models.traffic_sign_cnn import TrafficSignCNN
from traffic_sign_labels import GTSRB_LABELS, get_description


MODEL_PATH = Path("traffic_sign_cnn.pth")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

transform = transforms.Compose([
    transforms.Resize((32, 32)),
    transforms.ToTensor(),
])


def load_model():
    model = TrafficSignCNN(num_classes=43).to(device)

    if not MODEL_PATH.exists():
        return None

    model.load_state_dict(torch.load(MODEL_PATH, map_location=device))
    model.eval()
    return model


model = load_model()


def predict(image):
    if image is None:
        return "이미지를 업로드해 주세요."

    if model is None:
        return (
            "## 모델 파일이 없습니다.\n\n"
            "`traffic_sign_cnn.pth` 파일이 현재 폴더에 있어야 합니다.\n\n"
            "먼저 아래 명령어로 모델을 학습하세요.\n\n"
            "```bash\n"
            "python train_gtsrb_torch.py --epochs 5\n"
            "```"
        )

    image = Image.fromarray(image).convert("RGB")
    x = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        outputs = model(x)
        probabilities = torch.softmax(outputs, dim=1)[0]

    top_probs, top_indices = torch.topk(probabilities, k=3)

    best_idx = top_indices[0].item()
    best_label = GTSRB_LABELS[best_idx]
    best_confidence = top_probs[0].item() * 100

    lines = []
    lines.append("## 예측 결과")
    lines.append("")
    lines.append(f"**{best_label}**")
    lines.append(f"신뢰도: **{best_confidence:.2f}%**")
    lines.append("")
    lines.append("## 설명")
    lines.append(get_description(best_label))
    lines.append("")
    lines.append("## Top 3 예측")
    lines.append("")

    for rank, (prob, idx) in enumerate(zip(top_probs, top_indices), start=1):
        label = GTSRB_LABELS[idx.item()]
        confidence = prob.item() * 100
        lines.append(f"{rank}. **{label}** - {confidence:.2f}%")

    lines.append("")
    lines.append("---")
    lines.append("이 결과는 학습된 이미지 분류 모델의 예측이며, 실제 도로 상황에서는 참고용으로만 사용해야 한다.")

    return "\n".join(lines)


demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="numpy", label="교통 표지판 이미지 업로드"),
    outputs=gr.Markdown(label="분류 결과"),
    title="AI Traffic Sign Recognition",
    description=(
        "GTSRB 교통 표지판 데이터셋으로 학습한 CNN 모델을 이용해 "
        "업로드한 표지판 이미지를 43개 클래스 중 하나로 분류합니다."
    ),
    examples=None,
)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))

    print("Starting Gradio app...")
    print("PORT =", port)
    print("MODEL EXISTS =", MODEL_PATH.exists())
    print("DEVICE =", device)

    demo.queue()

    demo.launch(
        server_name="0.0.0.0",
        server_port=port,
        share=False,
        show_error=True
    )
