from core.action import Action

a = Action(
    action="click",
    target="Search Box"
)

print(a)

b = Action(
    action="type",
    text="robotics"
)

print(b)

c = Action(
    action="press",
    key="enter"
)

print(c)