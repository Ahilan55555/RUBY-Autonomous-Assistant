from modules.agents.task_inference_agent import (
    TaskInferenceAgent
)

agent = (
    TaskInferenceAgent()
)

print(
    agent.infer(
        [
            "Working on AI Assistant project"
        ],
        [
            "Python related work detected"
        ],
        [
            "Editing OCR code"
        ]
    )
)