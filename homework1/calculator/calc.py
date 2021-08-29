# please create your own git repository on github.
# (optional) setup pre-commit hook with black and isort formatting for the repo
# initialize .gitignore in the repository root (you can use this sample)
# create a homework1 directory in the repo
# then copy the sample_project into the directory.
# fix all bugs in the sample_project code
# write an extra test for each found bug

def check_power_of_2(a: int) -> bool:
    if a == 0:
        return False
    return not (bool(a & (a - 1)))
