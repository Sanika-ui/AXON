import os
import importlib

SKILLS = []

def load_skills():
    skills_folder = os.path.join(os.path.dirname(__file__), "skills")

    for filename in os.listdir(skills_folder):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = f"skills.{filename[:-3]}"   # correct import path
            module = importlib.import_module(module_name)
            SKILLS.append(module)

load_skills()

def process_command(command):
    for skill in SKILLS:
        if skill.can_handle(command):
            return skill.name, skill.handle(command)

    return "unknown", "I don't have that skill yet."
