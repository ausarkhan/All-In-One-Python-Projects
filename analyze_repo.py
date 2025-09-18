#!/usr/bin/env python3
"""
Repository Analysis Tool
Helps analyze your forked repository and find completed work
"""

import subprocess
import sys
import json
from datetime import datetime

def run_git_command(cmd):
    """Run a git command and return the output"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd='.')
        return result.stdout.strip(), result.stderr.strip(), result.returncode
    except Exception as e:
        return "", str(e), 1

def analyze_repository():
    """Analyze the repository structure and branches"""
    print("🔍 Repository Analysis Tool")
    print("=" * 50)
    
    # Check current status
    print("\n📍 Current Repository Status:")
    stdout, stderr, code = run_git_command("git status --porcelain")
    if code == 0:
        if stdout:
            print("⚠️  Working directory has uncommitted changes:")
            print(stdout)
        else:
            print("✅ Working directory is clean")
    
    # Show current branch
    stdout, stderr, code = run_git_command("git branch --show-current")
    if code == 0:
        print(f"📌 Current branch: {stdout}")
    
    # Show all remotes
    print("\n🌐 Remote Repositories:")
    stdout, stderr, code = run_git_command("git remote -v")
    if code == 0:
        for line in stdout.split('\n'):
            if line.strip():
                print(f"   {line}")
    
    # Show all branches
    print("\n🌿 All Branches:")
    stdout, stderr, code = run_git_command("git branch -a")
    if code == 0:
        branches = []
        for line in stdout.split('\n'):
            if line.strip():
                branches.append(line.strip())
        
        local_branches = [b for b in branches if not b.startswith('remotes/')]
        remote_branches = [b for b in branches if b.startswith('remotes/')]
        
        print("   Local branches:")
        for branch in local_branches:
            marker = "👉" if branch.startswith('*') else "  "
            print(f"   {marker} {branch.replace('* ', '')}")
        
        print("   Remote branches:")
        for branch in remote_branches:
            print(f"     {branch}")
    
    # Show recent commits on current branch
    print(f"\n📝 Recent Commits on Current Branch:")
    stdout, stderr, code = run_git_command("git log --oneline -10")
    if code == 0:
        for line in stdout.split('\n'):
            if line.strip():
                print(f"   {line}")
    
    # Try to compare with upstream if it exists
    print(f"\n🔄 Comparing with Upstream (if available):")
    
    # First check if upstream exists
    stdout, stderr, code = run_git_command("git remote get-url upstream")
    if code != 0:
        print("   ⚠️  Upstream remote not configured")
        print("   💡 Consider adding upstream: git remote add upstream https://github.com/king04aman/All-In-One-Python-Projects.git")
    else:
        print(f"   ✅ Upstream configured: {stdout}")
        
        # Check if upstream/main exists
        stdout, stderr, code = run_git_command("git rev-parse --verify upstream/main")
        if code != 0:
            print("   ⚠️  Upstream/main not available. Try: git fetch upstream")
        else:
            # Compare current branch with upstream/main
            stdout, stderr, code = run_git_command("git log upstream/main..HEAD --oneline")
            if code == 0:
                if stdout.strip():
                    print("   📊 Commits ahead of upstream/main:")
                    commit_count = len([l for l in stdout.split('\n') if l.strip()])
                    print(f"   🔢 {commit_count} commits ahead")
                    for line in stdout.split('\n'):
                        if line.strip():
                            print(f"     {line}")
                else:
                    print("   ✅ No commits ahead of upstream/main")
            else:
                print(f"   ⚠️  Error comparing with upstream: {stderr}")
    
    # Show what files have been added/modified compared to upstream
    print(f"\n📁 Files Added/Modified (compared to upstream if available):")
    stdout, stderr, code = run_git_command("git rev-parse --verify upstream/main")
    if code == 0:
        stdout, stderr, code = run_git_command("git diff upstream/main --name-status")
        if code == 0 and stdout.strip():
            added_files = []
            modified_files = []
            for line in stdout.split('\n'):
                if line.strip():
                    parts = line.split('\t')
                    if len(parts) >= 2:
                        status = parts[0]
                        filename = parts[1]
                        if status == 'A':
                            added_files.append(filename)
                        elif status == 'M':
                            modified_files.append(filename)
            
            if added_files:
                print("   📄 New files added:")
                for file in added_files:
                    print(f"     + {file}")
            
            if modified_files:
                print("   ✏️  Files modified:")
                for file in modified_files:
                    print(f"     ~ {file}")
            
            if not added_files and not modified_files:
                print("   📭 No files added or modified compared to upstream")
        else:
            print("   📭 No files added or modified compared to upstream")
    else:
        print("   ⚠️  Cannot compare with upstream - upstream/main not available")
    
    # Provide recommendations
    print(f"\n💡 Recommendations:")
    print("   1. If you have a branch with completed issues, switch to it using:")
    print("      git checkout <branch-name>")
    print("   2. To see commits on a specific branch:")
    print("      git log --oneline <branch-name>")
    print("   3. To see what files you've changed:")
    print("      git diff upstream/main --name-only")
    print("   4. Read FORK_MANAGEMENT_GUIDE.md for detailed instructions")

def main():
    """Main function"""
    analyze_repository()
    
    print(f"\n🎯 Next Steps:")
    print("   • Run this script from your repository directory")
    print("   • Check the FORK_MANAGEMENT_GUIDE.md file for detailed instructions")
    print("   • If you need to find a specific branch with your completed work:")
    print("     git branch -r | grep origin")

if __name__ == "__main__":
    main()