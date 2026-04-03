import subprocess
import json
from datetime import datetime

def get_git_log():
    """Read real git log and convert to JSON for the website"""
    
    result = subprocess.run(
        ['git', 'log', '--pretty=format:%h|%an|%ae|%ad|%s', '--date=format:%Y-%m-%d %H:%M:%S', '--name-only'],
        capture_output=True, text=True
    )
    
    lines   = result.stdout.strip().split('\n')
    commits = []
    i       = 0

    while i < len(lines):
        line = lines[i].strip()
        if '|' in line:
            parts  = line.split('|')
            if len(parts) >= 5:
                commit_id = parts[0]
                author    = parts[1]
                email     = parts[2]
                date      = parts[3]
                message   = parts[4]

                # Collect changed files
                files = []
                i += 1
                while i < len(lines) and lines[i].strip() and '|' not in lines[i]:
                    files.append(lines[i].strip())
                    i += 1

                if not files:
                    files = ['(no files listed)']

                commits.append({
                    'id':      commit_id,
                    'author':  author,
                    'email':   email,
                    'date':    date,
                    'message': message,
                    'files':   files,
                    'status':  'modified'
                })
        else:
            i += 1

    return commits

def generate_report():
    commits = get_git_log()
    
    # Save as JSON
    with open('git_log.json', 'w') as f:
        json.dump(commits, f, indent=2)
    
    print(f"✅ Report generated! Found {len(commits)} commits.")
    print("📄 Saved to git_log.json")
    
    # Print summary
    print("\n--- Audit Summary ---")
    authors = {}
    for c in commits:
        authors[c['author']] = authors.get(c['author'], 0) + 1
    
    for author, count in authors.items():
        print(f"  {author}: {count} commits")

if __name__ == '__main__':
    generate_report()