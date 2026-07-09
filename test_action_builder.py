from core.action_builder import ActionBuilder

builder = ActionBuilder()

print(builder.type("Hello"))

print(builder.press("enter"))

print(builder.wait(1))