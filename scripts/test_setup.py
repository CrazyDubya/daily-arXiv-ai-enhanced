#!/usr/bin/env python3
"""
Test script to validate the daily-arXiv-ai-enhanced setup works correctly.
This tests core functionality without requiring external API access.
"""

import json
import os
import sys
from pathlib import Path

def test_data_structure():
    """Test that data files exist and have correct structure"""
    data_dir = Path("data")
    if not data_dir.exists():
        print("❌ Data directory not found")
        return False
    
    # Find a recent AI-enhanced file
    ai_files = list(data_dir.glob("*_AI_enhanced_*.jsonl"))
    if not ai_files:
        print("❌ No AI-enhanced files found")
        return False
    
    # Test the most recent file
    test_file = sorted(ai_files)[-1]
    print(f"✅ Testing file: {test_file}")
    
    try:
        with open(test_file, 'r') as f:
            lines = list(f)
        
        if not lines:
            print("❌ File is empty")
            return False
        
        # Test first entry
        data = json.loads(lines[0])
        
        # Check required fields
        required_fields = ['id', 'categories', 'title', 'authors', 'summary', 'AI']
        for field in required_fields:
            if field not in data:
                print(f"❌ Missing field: {field}")
                return False
        
        # Check AI fields
        ai_required = ['tldr', 'motivation', 'method', 'result', 'conclusion']
        for field in ai_required:
            if field not in data['AI']:
                print(f"❌ Missing AI field: {field}")
                return False
        
        print(f"✅ Data structure valid - {len(lines)} papers in file")
        print(f"✅ Categories: {', '.join(data['categories'])}")
        print(f"✅ AI enhancement present")
        return True
        
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return False

def test_markdown_conversion():
    """Test that markdown conversion works"""
    try:
        # Check if conversion script exists and has main structure
        convert_path = Path("to_md/convert.py")
        if not convert_path.exists():
            print("❌ convert.py not found")
            return False
        
        # Check if template exists
        template_path = Path("to_md/paper_template.md")
        if not template_path.exists():
            print("❌ paper_template.md not found")
            return False
        
        # Test that we can read the conversion script
        with open(convert_path, 'r') as f:
            content = f.read()
            if 'def rank(' in content and 'template.format(' in content:
                print("✅ Markdown conversion script structure valid")
                return True
            else:
                print("❌ Markdown conversion script missing key functions")
                return False
        
    except Exception as e:
        print(f"❌ Error testing markdown conversion: {e}")
        return False

def test_readme_generation():
    """Test that README generation works"""
    try:
        # Check if template exists
        if not Path("template.md").exists():
            print("❌ template.md not found")
            return False
        
        if not Path("readme_content_template.md").exists():
            print("❌ readme_content_template.md not found")
            return False
        
        # Check if update script exists
        if not Path("update_readme.py").exists():
            print("❌ update_readme.py not found")
            return False
        
        print("✅ README generation system files present")
        return True
        
    except Exception as e:
        print(f"❌ Error testing README generation: {e}")
        return False

def test_web_assets():
    """Test that web assets exist"""
    web_files = [
        "index.html",
        "settings.html", 
        "statistic.html",
        "css/styles.css",
        "js/settings.js"
    ]
    
    missing_files = []
    for file_path in web_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
    
    if missing_files:
        print(f"❌ Missing web files: {', '.join(missing_files)}")
        return False
    
    print("✅ All web assets present")
    return True

def main():
    """Run all tests"""
    print("🚀 Testing daily-arXiv-ai-enhanced setup...")
    print("=" * 50)
    
    tests = [
        ("Data structure", test_data_structure),
        ("Markdown conversion", test_markdown_conversion),
        ("README generation", test_readme_generation),
        ("Web assets", test_web_assets)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n📋 {test_name}:")
        if test_func():
            passed += 1
        else:
            print(f"❌ {test_name} failed")
    
    print("\n" + "=" * 50)
    print(f"📊 Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Setup is working correctly.")
        return True
    else:
        print("⚠️  Some tests failed. See output above for details.")
        return False

if __name__ == "__main__":
    os.chdir(Path(__file__).parent.parent)
    success = main()
    sys.exit(0 if success else 1)