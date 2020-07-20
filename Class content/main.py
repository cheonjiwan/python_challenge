from indeed import main as get_indeed_jobs
from stackoverflow import main as get_so_jobs
from save import save_to_file

so_jobs = get_so_jobs()
indeed_jobs = get_indeed_jobs()
jobs = indeed_jobs
save_to_file(jobs)