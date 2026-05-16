import requests
import matplotlib.pyplot as plt
from collections import Counter

# Fetch data from Codeforces API
response = requests.get("https://codeforces.com/api/user.status?handle=CoderSadanand").json()

if response['status'] == 'OK':
    solved_problems = set()
    ratings = []
    
    # Filter for unique, accepted problems that have a rating
    for sub in response['result']:
        if sub['verdict'] == 'OK' and 'rating' in sub['problem']:
            prob_id = f"{sub['problem'].get('contestId')}{sub['problem'].get('index')}"
            if prob_id not in solved_problems:
                solved_problems.add(prob_id)
                ratings.append(sub['problem']['rating'])
                
    # Count frequencies of each rating
    rating_counts = Counter(ratings)
    labels = sorted(rating_counts.keys())
    values = [rating_counts[r] for r in labels]
    
    # Generate the bar chart
    plt.style.use('dark_background')
    plt.figure(figsize=(10, 4))
    plt.bar(labels, values, width=60, color='#00ff88', edgecolor='black')
    
    plt.xlabel('Problem Rating', fontsize=12)
    plt.ylabel('Problems Solved', fontsize=12)
    plt.title('Codeforces Problem Rating Distribution', fontsize=14, pad=15)
    plt.grid(axis='y', alpha=0.2)
    
    # Save as a transparent SVG
    plt.savefig('cf_graph.svg', format='svg', transparent=True, bbox_inches='tight')