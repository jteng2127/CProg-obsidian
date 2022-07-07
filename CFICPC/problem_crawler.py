from bs4 import BeautifulSoup
import requests
import os
import datetime

root_dir = r'CFICPC'
cf_prefix = r'https://codeforces.com'
gym_prefix = r'/gym/'
prob_prefix = r'/problem/'

def fetch_all_problem_by_enumeration(contest_id, contest_soup, contest_file):
  problem_id = 'A'
  while True:
    problem_url = cf_prefix + gym_prefix + contest_id + prob_prefix + problem_id
    problem_response = requests.get(problem_url)
    problem_soup = BeautifulSoup(problem_response.text, 'html.parser')
    is_problem_exist = True
    try:
      if problem_soup.title.text == 'Codeforces':
        is_problem_exist = False
    except:
      pass
    if not is_problem_exist: break
    # print(f'fetching {problem_id}')

    # get problem title
    problem_title = contest_soup.find_all('a', {'href': gym_prefix + contest_id + prob_prefix + problem_id})[1].text
    problem_title = f'{problem_id} - {problem_title}'

    # write problem file 
    with open(os.path.join(contest_id, f'{problem_id}.md'), 'w', encoding='utf-8') as problem_file:
      problem_file.write(f'# {problem_title}\n\n')
      problem_file.write(f'url: {problem_url}\n')
      problem_file.write(f'Status: #UNSOLVED\n')
      problem_file.write(f'Tags: #\n\n')
      problem_file.write(f'## Description\n\n')
      problem_file.write(f'## Solution\n\n')
    
    # write problem into contest file
    contest_file.write(f'* [[{root_dir}/{contest_id}/{problem_id}|{problem_title}]]\n')

    # next problem
    problem_id = chr(ord(problem_id) + 1)

def fetch_all_problem_by_table(contest_id, contest_soup, contest_file, contest_title):
  problem_table = contest_soup.find('table', {'class': 'problems'})
  for idx, problem_row in enumerate(problem_table.find_all('tr')[1:]):
    all_problem_info = problem_row.find_all('a')
    del all_problem_info[2]
    problem_id = all_problem_info[0].text.strip()
    problem_title = f'{problem_id} - {all_problem_info[1].text}'
    try:
      problem_solved_number = all_problem_info[2].text.strip()
      problem_solved_number = problem_solved_number[1:]
    except:
      problem_solved_number = '0'
    problem_url = cf_prefix + gym_prefix + contest_id + prob_prefix + problem_id

    # write problem file 
    with open(os.path.join(contest_id, f'{problem_id}.md'), 'w', encoding='utf-8') as problem_file:
      problem_file.write(f'# {problem_title}\n\n')
      problem_file.write(f'contest: [[{root_dir}/{contest_id}/{contest_id}|{contest_title}]]\n')
      problem_file.write(f'url: {problem_url}\n')
      problem_file.write(f'Status: #UNSOLVED\n')
      problem_file.write(f'Tags: #\n\n')
      problem_file.write(f'## Description\n\n')
      problem_file.write(f'## Solution\n\n')
    
    # write problem into contest file
    contest_file.write(f'|{idx+1}|[[{root_dir}/{contest_id}/{problem_id}\|{problem_title}]]|{problem_solved_number}|\n')

with open('all_contest_id.txt', 'r', encoding='utf-8') as all_contest_id_file:
  contest_id_update_time = all_contest_id_file.readline()
  # open all contest file
  with open('CFICPC_all_contest.md', 'w', encoding='utf-8') as all_contest_file:
    # write all contest file
    all_contest_file.write('# All Codeforces ICPC Contests\n\n')
    # all_contest_file.write('updated at: ' + contest_id_update_time + '\n')
    all_contest_file.write('updated at: ' + str(datetime.datetime.now()) + '\n')
    all_contest_file.write('filterContestType=Official ACM-ICPC Contest & order=ID_DESC\n\n')
    all_contest_file.write('## Contests\n\n')

    # fetch all contest id
    all_contest_id = all_contest_id_file.read().splitlines()
    for idx, contest_id in enumerate(all_contest_id):
      try:
        # create directory
        if not os.path.exists(contest_id):
          os.makedirs(contest_id)

        # open contest file
        with open(f'{contest_id}/{contest_id}.md', 'w', encoding='utf-8') as contest_file:
          print(f'fetching {contest_id} ({idx+1}/{len(all_contest_id)})')
          contest_url = cf_prefix + gym_prefix + contest_id
          contest_response = requests.get(contest_url)
          contest_soup = BeautifulSoup(contest_response.text, 'lxml')

          # write contest title
          contest_title = contest_soup.find('a', {'href': gym_prefix + contest_id}).text
          contest_file.write(f'# {contest_title}\n\n')
          contest_file.write(f'url: {contest_url}\n')
          contest_file.write(f'[search solutions](https://www.google.com/search?q=Solution+OR+題解+{"+".join(contest_title.replace("+", "%2B").split(" "))})\n\n')
          contest_file.write(f'## Problems\n\n')
          # write table title
          contest_file.write('| # | Title | Solved |\n')
          contest_file.write('| --- | --- | --- |\n')

          # write contest title into all contest file
          all_contest_file.write(f'{idx+1}. [[{root_dir}/{contest_id}/{contest_id}|{contest_title}]]\n')
          
          # fetch all problem in contest
          # fetch_all_problem_by_enumeration(contest_id, contest_soup, contest_file)
          fetch_all_problem_by_table(contest_id, contest_soup, contest_file, contest_title)

          # fetch done
          print(f'{contest_id} done')
      except IndexError as e:
        print(f'{contest_id} failed')
        all_contest_file.write(f'fail: {contest_id}\n')
        continue
