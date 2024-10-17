import matplotlib.pyplot as plt

def plot_esg_data(company, esg_data):
    labels = ['Environmental', 'Social', 'Governance']
    scores = [esg_data['environmental'], esg_data['social'], esg_data['governance']]

    plt.bar(labels, scores, color=['green', 'blue', 'orange'])
    plt.title(f"{company} ESG Metrics")
    plt.xlabel('Category')
    plt.ylabel('Score')
    plt.show()

# Example usage
company = 'Apple'
esg_data = {
    'environmental': 80,
    'social': 75,
    'governance': 79
}

plot_esg_data(company, esg_data)
