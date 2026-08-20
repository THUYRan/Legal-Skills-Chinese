#!/usr/bin/env python3
"""
Lint and validate all skills in the Legal-Skills-Chinese repository.

Checks:
1. Skill directory name is lowercase-hyphenated slug.
2. SKILL.md exists in each skill directory.
3. SKILL.md has valid YAML frontmatter containing 'name' and 'description'.
4. Frontmatter 'name' matches the directory name exactly.
5. Markdown code blocks (```) are properly paired and closed.
6. Skill links in README.md and README_EN.md resolve to existing directories.
"""

import os
import re
import sys

def main():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    skills_dir = os.path.join(repo_root, 'skills')
    
    if not os.path.isdir(skills_dir):
        print(f"Error: skills directory not found at {skills_dir}")
        sys.exit(1)
        
    skill_dirs = sorted([d for d in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, d))])
    
    errors = []
    slug_pattern = re.compile(r'^[a-z0-9]+(-[a-z0-9]+)*$')
    
    print(f"🔍 Auditing {len(skill_dirs)} skill directories in {skills_dir}...\n")
    
    for s_name in skill_dirs:
        s_path = os.path.join(skills_dir, s_name)
        
        # Check 1: Directory naming
        if not slug_pattern.match(s_name):
            errors.append(f"[{s_name}] Directory name '{s_name}' is not a valid lowercase-hyphenated slug.")
            
        skill_md = os.path.join(s_path, 'SKILL.md')
        
        # Check 2: SKILL.md exists
        if not os.path.isfile(skill_md):
            errors.append(f"[{s_name}] Missing SKILL.md in {s_path}")
            continue
            
        with open(skill_md, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Check 3: YAML frontmatter
        if not content.startswith('---'):
            errors.append(f"[{s_name}] SKILL.md does not start with YAML frontmatter ('---').")
            continue
            
        parts = content.split('---', 2)
        if len(parts) < 3:
            errors.append(f"[{s_name}] SKILL.md has unclosed YAML frontmatter (missing closing '---').")
            continue
            
        fm_text = parts[1]
        
        # Check 4: 'name' field in frontmatter
        name_match = re.search(r'^\s*name:\s*([^\n\r]+)', fm_text, re.MULTILINE)
        if not name_match:
            errors.append(f"[{s_name}] Frontmatter missing 'name' field.")
        else:
            fm_name = name_match.group(1).strip().strip('"\'')
            if fm_name != s_name:
                errors.append(f"[{s_name}] Frontmatter name '{fm_name}' does not match directory name '{s_name}'.")
                
        # Check 5: 'description' field in frontmatter
        desc_match = re.search(r'^\s*description:\s*(.+)', fm_text, re.MULTILINE)
        if not desc_match:
            errors.append(f"[{s_name}] Frontmatter missing 'description' field.")
            
        # Check 6: Markdown code block balance
        code_block_count = content.count('```')
        if code_block_count % 2 != 0:
            errors.append(f"[{s_name}] Unbalanced markdown code blocks (found {code_block_count} '```' markers).")

    # Check 7: Documentation links
    for readme_filename in ['README.md', 'README_EN.md']:
        readme_path = os.path.join(repo_root, readme_filename)
        if os.path.exists(readme_path):
            with open(readme_path, 'r', encoding='utf-8') as f:
                readme_content = f.read()
            links = re.findall(r'\]\((?:\./)?skills/([a-zA-Z0-9_-]+)(?:/)?\)', readme_content)
            for target_dir in links:
                full_target = os.path.join(skills_dir, target_dir)
                if not os.path.exists(full_target):
                    errors.append(f"[{readme_filename}] Broken link pointing to non-existent directory: skills/{target_dir}")

    # Summary
    if errors:
        print(f"❌ Found {len(errors)} error(s):")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print(f"✅ All {len(skill_dirs)} skills passed validation successfully!")
        sys.exit(0)

if __name__ == '__main__':
    main()
