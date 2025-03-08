# KPMClub-KPMClub.github.io

This repository hosts the official website of the **Kun Peng Maker Club (KPMClub)**.

---

## How to Post a Blog

If you want to publish a new blog post, follow these steps:

### 1. Write Your Blog in Markdown
- Create a new Markdown file (`.md`) for your blog post.
- Place the file in the `blogs` folder.
- The file name should follow this format:  
  `YYYY-MM-DD-Title.md`  
  For example: `2023-10-15-How-to-Use-Markdown.md`

### 2. Convert Markdown to HTML
- Use the `md_to_html.py` script to convert your Markdown file into an HTML file.
  - Ensure you have installed the required Python libraries:
    ```bash
    pip install markdown beautifulsoup4
    ```
  - Run the script:
    ```bash
    python md_to_html.py
    ```
- The script will generate an HTML file in the `blog-detail` folder with the same name as your Markdown file (e.g., `2023-10-15-How-to-Use-Markdown.html`).

### 3. Commit and Push Changes
- Use Git to add, commit, and push your changes:
  ```bash
  git add blogs/2023-10-15-Title.md blog-detail/2023-10-15-Title.html
  git commit -m "Add new blog: 2023-10-15-Title"
  git push origin main
