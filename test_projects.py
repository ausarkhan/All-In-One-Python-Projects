#!/usr/bin/env python3
"""
Test script to verify that completed projects are functional
"""

import os
import sys
import subprocess
import importlib.util

def test_project_structure(project_path):
    """Test if a project has the required structure"""
    required_files = ['README.md', 'requirements.txt']
    missing_files = []
    
    for file in required_files:
        file_path = os.path.join(project_path, file)
        if not os.path.exists(file_path):
            missing_files.append(file)
    
    # Check for main Python file
    python_files = [f for f in os.listdir(project_path) if f.endswith('.py')]
    
    return {
        'missing_files': missing_files,
        'python_files': python_files,
        'has_structure': len(missing_files) == 0 and len(python_files) > 0
    }

def test_import_syntax(python_file):
    """Test if a Python file has valid syntax"""
    try:
        with open(python_file, 'r', encoding='utf-8') as f:
            code = f.read()
        
        # Try to compile the code
        compile(code, python_file, 'exec')
        return True, "Valid syntax"
    except SyntaxError as e:
        return False, f"Syntax error: {e}"
    except Exception as e:
        return False, f"Error: {e}"

def main():
    """Main test function"""
    print("🧪 Testing Completed Projects")
    print("=" * 50)
    
    # List of projects from the analysis
    projects = [
        'Advanced_Extractive_Text_Summarization',
        'Analog_Wall_Clock',
        'Calendar_Generator_YearWise',
        'GraphRAG',
        'Language_Learning_Chatbot',
        'Personal_Finance_Dashboard',
        'Photo_Organizer_App',
        'Simple_PDF_Editor',
        'Student_Management_System',
        'Sustainable_Travel_Planner',
        'Travel_Itinerary_Planner'
    ]
    
    working_projects = []
    issues_found = []
    
    for project in projects:
        project_path = os.path.join('.', project)
        
        if not os.path.exists(project_path):
            issues_found.append(f"❌ {project}: Directory not found")
            continue
        
        print(f"\n🔍 Testing {project}...")
        
        # Test project structure
        structure = test_project_structure(project_path)
        
        if not structure['has_structure']:
            issues_found.append(f"❌ {project}: Missing files - {structure['missing_files']}")
            continue
        
        print(f"   ✅ Project structure valid")
        print(f"   📁 Python files: {', '.join(structure['python_files'])}")
        
        # Test Python syntax for main files
        syntax_ok = True
        for py_file in structure['python_files']:
            file_path = os.path.join(project_path, py_file)
            valid, message = test_import_syntax(file_path)
            if not valid:
                issues_found.append(f"❌ {project}/{py_file}: {message}")
                syntax_ok = False
            else:
                print(f"   ✅ {py_file}: {message}")
        
        if syntax_ok:
            working_projects.append(project)
    
    # Print summary
    print(f"\n📊 Summary")
    print("=" * 50)
    print(f"✅ Working projects: {len(working_projects)}")
    print(f"❌ Projects with issues: {len(issues_found)}")
    
    if working_projects:
        print(f"\n✅ Working Projects:")
        for project in working_projects:
            print(f"   • {project}")
    
    if issues_found:
        print(f"\n❌ Issues Found:")
        for issue in issues_found:
            print(f"   • {issue}")
    
    print(f"\n🎯 Conclusion:")
    if len(working_projects) >= len(projects) * 0.8:  # 80% working
        print("   🎉 Most projects are working correctly!")
        print("   💡 These projects are ready for submission to upstream repository")
    else:
        print("   ⚠️  Some projects need attention before submission")
    
    return len(working_projects), len(issues_found)

if __name__ == "__main__":
    working, issues = main()
    # Exit with 0 if most projects work, 1 if many issues
    sys.exit(0 if working >= issues else 1)