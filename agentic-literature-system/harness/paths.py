from pathlib import Path

ROOT = Path(__file__).resolve().parent
SKILL = ROOT.parent / "skill"

def resource_name(path, root=ROOT, skill=SKILL):
    path = Path(path).resolve()
    if path.is_relative_to(skill.resolve()):
        return "skill/" + str(path.relative_to(skill.resolve()))
    return str(path.relative_to(root.resolve()))
