# Metrics-Center

**Evaluate, compare, and visualize clustering algorithms with ease.**

Metrics-Center is a full-stack web application designed for data scientists, machine learning practitioners, researchers, and students who need to **quickly evaluate and compare unsupervised clustering algorithms** on their datasets. It provides an intuitive interface to upload data, configure clustering models, run evaluations, compute standard internal and external validation metrics, and visualize results interactively — all without writing a single line of code.

Whether you're exploring the best clustering approach for a new dataset, teaching clustering concepts, or benchmarking algorithms in a research project, Metrics-Center saves time and delivers clear, reproducible insights.

## Motivation

Clustering is a fundamental unsupervised learning task, but evaluating clustering quality is notoriously challenging:
- There is no single "best" algorithm — performance depends heavily on data distribution and hyperparameters.
- Computing and interpreting validation metrics (Silhouette, Davies-Bouldin, etc.) requires boilerplate code.
- Visualizing clusters, elbow curves, and silhouette plots helps build intuition but is tedious to implement repeatedly.
- Reproducing experiments across multiple datasets or parameter settings often leads to scattered notebooks and scripts.

**Metrics-Center solves these problems** by offering a dedicated, user-friendly platform for clustering experimentation with built-in support for metrics, visualizations, project management, and report export.

## Features

### Core Functionality
- **Supported Algorithms**: K-Means, DBSCAN, Agglomerative Clustering (Hierarchical), and more via scikit-learn.
- **Evaluation Metrics**:
  - Internal: Silhouette Score, Davies-Bouldin Index, Calinski-Harabasz Score, Dunn Index
  - External (when ground-truth labels provided): Adjusted Rand Index (ARI), Normalized Mutual Information (NMI)
- **Interactive Visualizations** (powered by Plotly):
  - Scatter plots colored by cluster assignment (2D/3D with PCA/TSNE reduction)
  - Elbow plots (for K-Means)
  - Silhouette plots
  - Cluster dendrograms (for hierarchical clustering)

### Data Import
- Upload local files: CSV, Excel (.xlsx, .xls)
- Direct import from **Google Drive** using OAuth2 and Google Picker API
- Built-in sample datasets (Iris, Wine, MNIST subset, etc.) for instant testing

### Project Management
- Create and save multiple projects
- Organize datasets, evaluations, and results
- View full history of evaluations per project
- Revisit and compare past runs

### Export & Reporting
- Download metrics as CSV
- Export individual plots as PNG
- Generate complete PDF reports (metrics + visualizations) using WeasyPrint

### User Experience
- Clean, modern, responsive UI built with React + Tailwind CSS
- Dark mode support
- Loading states, error handling, and toast notifications
- Secure authentication (JWT-based login/register)

### Technical Highlights
- **Backend**: FastAPI (Python) – fast, type-safe, async-ready
- **Frontend**: React + Vite + Tailwind CSS + TanStack Query
- **Database**: SQLite for development, easily switchable to PostgreSQL
- **Background Processing**: Support for long-running clustering jobs (Celery + Redis ready)
- **Deployment**: Fully Dockerized with docker-compose

## Repository Structure
