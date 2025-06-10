#!/usr/bin/env python3
"""
Test script to verify Superagent deployment configuration
"""

import os
import sys
import subprocess
import time
import requests
from pathlib import Path

def test_backend_dockerfile():
    """Test if backend Dockerfile has correct configuration"""
    dockerfile_path = Path("libs/superagent/Dockerfile")
    if not dockerfile_path.exists():
        print("❌ Backend Dockerfile not found")
        return False
    
    content = dockerfile_path.read_text()
    
    # Check for correct gunicorn binding
    if "--bind 0.0.0.0:$PORT" in content or "./start.sh" in content:
        print("✅ Backend Dockerfile has correct port binding")
        return True
    else:
        print("❌ Backend Dockerfile missing correct port binding")
        return False

def test_frontend_dockerfile():
    """Test if frontend Dockerfile has correct configuration"""
    dockerfile_path = Path("libs/ui/Dockerfile")
    if not dockerfile_path.exists():
        print("❌ Frontend Dockerfile not found")
        return False
    
    content = dockerfile_path.read_text()
    
    # Check for correct Next.js binding
    if "-H 0.0.0.0" in content and "${PORT:-3000}" in content:
        print("✅ Frontend Dockerfile has correct port binding")
        return True
    else:
        print("❌ Frontend Dockerfile missing correct port binding")
        return False

def test_render_config():
    """Test if render.yaml exists and has correct structure"""
    render_config = Path("render.yaml")
    if not render_config.exists():
        print("❌ render.yaml not found")
        return False
    
    content = render_config.read_text()
    
    # Check for required configurations
    checks = [
        ("services:", "Services section"),
        ("type: web", "Web service type"),
        ("env: docker", "Docker environment"),
        ("healthCheckPath: /health", "Health check path"),
        ("PORT", "PORT environment variable")
    ]
    
    all_passed = True
    for check, description in checks:
        if check in content:
            print(f"✅ {description} found in render.yaml")
        else:
            print(f"❌ {description} missing in render.yaml")
            all_passed = False
    
    return all_passed

def test_startup_script():
    """Test if startup script exists and is executable"""
    script_path = Path("libs/superagent/start.sh")
    if not script_path.exists():
        print("❌ Startup script not found")
        return False
    
    if os.access(script_path, os.X_OK):
        print("✅ Startup script is executable")
        return True
    else:
        print("❌ Startup script is not executable")
        return False

def test_health_endpoint():
    """Test if health endpoint is added to routers"""
    router_path = Path("libs/superagent/app/routers.py")
    if not router_path.exists():
        print("❌ Router file not found")
        return False
    
    content = router_path.read_text()
    
    if "/health" in content and "health_check" in content:
        print("✅ Health check endpoint added to routers")
        return True
    else:
        print("❌ Health check endpoint missing from routers")
        return False

def main():
    """Run all tests"""
    print("🧪 Testing Superagent Render Deployment Configuration\n")
    
    tests = [
        ("Backend Dockerfile", test_backend_dockerfile),
        ("Frontend Dockerfile", test_frontend_dockerfile),
        ("Render Configuration", test_render_config),
        ("Startup Script", test_startup_script),
        ("Health Endpoint", test_health_endpoint),
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n📋 Testing {test_name}:")
        result = test_func()
        results.append((test_name, result))
    
    print("\n" + "="*50)
    print("📊 TEST RESULTS SUMMARY")
    print("="*50)
    
    passed = 0
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name}")
        if result:
            passed += 1
    
    print(f"\n🎯 {passed}/{len(tests)} tests passed")
    
    if passed == len(tests):
        print("\n🎉 All tests passed! Your Superagent deployment should work on Render.")
        print("\n📝 Next steps:")
        print("1. Commit and push these changes to your repository")
        print("2. Deploy using render.yaml or manual configuration")
        print("3. Set up required environment variables in Render dashboard")
        return True
    else:
        print("\n⚠️  Some tests failed. Please review the configuration.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)