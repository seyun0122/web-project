GTSRB_LABELS = [
    "Speed limit 20 km/h",
    "Speed limit 30 km/h",
    "Speed limit 50 km/h",
    "Speed limit 60 km/h",
    "Speed limit 70 km/h",
    "Speed limit 80 km/h",
    "End of speed limit 80 km/h",
    "Speed limit 100 km/h",
    "Speed limit 120 km/h",
    "No passing",
    "No passing for vehicles over 3.5 tons",
    "Right-of-way at intersection",
    "Priority road",
    "Yield",
    "Stop",
    "No vehicles",
    "Vehicles over 3.5 tons prohibited",
    "No entry",
    "General caution",
    "Dangerous curve left",
    "Dangerous curve right",
    "Double curve",
    "Bumpy road",
    "Slippery road",
    "Road narrows on right",
    "Road work",
    "Traffic signals",
    "Pedestrians",
    "Children crossing",
    "Bicycles crossing",
    "Beware of ice/snow",
    "Wild animals crossing",
    "End of all speed and passing limits",
    "Turn right ahead",
    "Turn left ahead",
    "Ahead only",
    "Go straight or right",
    "Go straight or left",
    "Keep right",
    "Keep left",
    "Roundabout mandatory",
    "End of no passing",
    "End of no passing by vehicles over 3.5 tons",
]


KOREAN_DESCRIPTIONS = {
    "Stop": "정지 표지판이다. 차량은 교차로나 정지선 앞에서 완전히 멈춰야 한다.",
    "Yield": "양보 표지판이다. 다른 차량이나 보행자에게 우선권을 양보해야 한다.",
    "No entry": "진입 금지 표지판이다. 해당 방향으로 차량이 들어가면 안 된다.",
    "Priority road": "우선도로 표지판이다. 이 도로를 주행하는 차량에 우선권이 있음을 의미한다.",
    "Traffic signals": "신호등 주의 표지판이다. 전방의 신호등 상태를 확인해야 한다.",
    "Pedestrians": "보행자 주의 표지판이다. 보행자 통행 가능성이 있으므로 속도를 줄여야 한다.",
    "Children crossing": "어린이 보호 또는 어린이 횡단 주의 표지판이다.",
    "Road work": "공사 구간 주의 표지판이다. 차선 변경이나 속도 저하가 필요할 수 있다.",
    "Slippery road": "미끄러운 도로 주의 표지판이다. 급제동과 급조향을 피해야 한다.",
    "Bicycles crossing": "자전거 횡단 주의 표지판이다.",
    "Roundabout mandatory": "회전교차로 진행 표지판이다.",
    "General caution": "일반 위험 주의 표지판이다. 전방 상황을 주의 깊게 확인해야 한다.",
}


def get_description(label: str) -> str:
    if label in KOREAN_DESCRIPTIONS:
        return KOREAN_DESCRIPTIONS[label]

    if label.startswith("Speed limit"):
        return "속도 제한 표지판이다. 표시된 제한 속도를 넘지 않도록 주행해야 한다."

    if label.startswith("Turn"):
        return "진행 방향 지시 표지판이다. 표시된 방향으로 진행해야 한다."

    if label.startswith("Keep"):
        return "차량이 지정된 방향을 따라 주행해야 함을 의미하는 표지판이다."

    if label.startswith("No passing"):
        return "추월 금지 표지판이다. 해당 구간에서는 앞 차량을 추월하면 안 된다."

    if label.startswith("End of"):
        return "기존 제한이나 금지 조건이 끝났음을 알리는 표지판이다."

    return "교통 표지판의 종류를 분류한 결과이다. 실제 도로 환경에서는 주변 상황과 함께 판단해야 한다."
