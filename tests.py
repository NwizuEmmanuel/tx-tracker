import subprocess
from main import app

def test_add_task():
    result = subprocess.run(
        ["py","main.py","--add","todo"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0

def test_list_tasks():
    result = subprocess.run(
        ["py","main.py","--list"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0

def test_update_task():
    result = subprocess.run(
        ["py","main.py","--list"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0

def test_delete_task():
    result = subprocess.run(
        ["py","main.py","--delete","1"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0

def test_mark_done():
    result = subprocess.run(
        ["py","main.py","-md", "1"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0

def test_mark_in_progress():
    result = subprocess.run(
        ["py","main.py","-mp","1"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0

def test_list_todo():
    result = subprocess.run(
        ["py","main.py","-lt"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0

def test_list_done():
    result = subprocess.run(
        ["py","main.py","-ld"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0

def test_list_in_progress():
    result = subprocess.run(
        ["py","main.py","-lp"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0

def test_delete_all_when_yes():
    result = subprocess.run(
        ["py","main.py","-da"],
        input="y\n",
        capture_output=True,
        text=True,
    )
    assert "Are you sure? (y/[n])" in result.stdout
    assert result.returncode == 0

def test_delete_all_when_no():
    result = subprocess.run(
        ["py","main.py","-da"],
        input="n\n",
        capture_output=True,
        text=True,
    )
    assert "Are you sure? (y/[n])" in result.stdout
    assert result.returncode == 0

def test_delete_all_when_empty():
    result = subprocess.run(
        ["py","main.py","-da"],
        input="\n",
        capture_output=True,
        text=True,
    )
    assert "Are you sure? (y/[n])" in result.stdout
    assert result.returncode == 0