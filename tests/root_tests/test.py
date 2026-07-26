from core.mission_context import MissionContext

context = MissionContext()

context.set(
    "paper_url",
    "https://..."
)

print(
    context.get(
        "paper_url"
    )
)