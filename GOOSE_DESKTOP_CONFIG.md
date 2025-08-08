# Goose Desktop Configuration Guide 🎯

This guide shows you exactly how to configure Goose Mentor Mode in Goose Desktop.

## 📋 Prerequisites

1. **Install the package first:**
   ```bash
   pip install goose-mentor-mode
   ```

2. **Verify installation:**
   ```bash
   pip show goose-mentor-mode
   ```

## 🎯 Method 1: Goose Desktop UI Configuration (Recommended)

### Step 1: Open Goose Desktop Settings
1. Launch Goose Desktop
2. Click the **⚙️ Settings** button (top-right corner)
3. Navigate to **Profiles** in the left sidebar

### Step 2: Select or Create a Profile
- **Option A**: Select an existing profile from the list
- **Option B**: Click **"+ New Profile"** to create a dedicated mentor profile

### Step 3: Add the Mentor Toolkit
1. In your profile settings, find the **"Toolkits"** section
2. Click **"+ Add Toolkit"**
3. Enter the toolkit details:
   ```
   Name: mentor
   Package: goose-mentor-mode
   ```
4. Click **"Add"** to save

### Step 4: Configure Environment Variables (Optional)
1. In the same profile, find the **"Environment Variables"** section
2. Click **"+ Add Variable"** for each configuration you want:

**For New Developer (Recommended starter configuration):**
```
DEFAULT_ASSISTANCE_LEVEL = guided
LEARNING_PHASE = skill_building
TIMELINE_PRESSURE = low
ENABLE_VALIDATION_CHECKPOINTS = true
MAX_GUIDANCE_DEPTH = 3
DEVELOPER_EXPERIENCE_MONTHS = 6
```

**For Experienced Developer:**
```
DEFAULT_ASSISTANCE_LEVEL = assisted
LEARNING_PHASE = production
TIMELINE_PRESSURE = medium
ENABLE_VALIDATION_CHECKPOINTS = false
MAX_GUIDANCE_DEPTH = 1
DEVELOPER_EXPERIENCE_MONTHS = 24
```

### Step 5: Save and Test
1. Click **"Save Profile"**
2. Select your profile in the main Goose interface
3. Test with a question like: *"How do I implement user authentication?"*

## 🔧 Method 2: Direct Configuration File Edit

### Step 1: Locate Your Config File
```bash
# macOS
~/.config/goose/config.yaml

# Windows
%APPDATA%\goose\config.yaml

# Linux
~/.config/goose/config.yaml
```

### Step 2: Edit the Configuration
Add or modify your profile configuration:

```yaml
# Example complete profile configuration
profiles:
  mentor-enabled:
    provider: "anthropic"
    processor: "gpt-4o"
    accelerator: null
    moderator: null
    toolkits:
      - name: "developer"
      - name: "mentor"
        package: "goose-mentor-mode"
    env:
      # Mentor Mode Configuration
      DEFAULT_ASSISTANCE_LEVEL: "guided"
      LEARNING_PHASE: "skill_building" 
      TIMELINE_PRESSURE: "low"
      ENABLE_VALIDATION_CHECKPOINTS: "true"
      MAX_GUIDANCE_DEPTH: "3"
      DEVELOPER_EXPERIENCE_MONTHS: "6"
```

### Step 3: Restart Goose Desktop
Close and reopen Goose Desktop for changes to take effect.

## ✅ Verification Steps

### Test 1: Basic Functionality
Ask Goose: *"How do I create a REST API?"*

**Expected with Mentor Mode:**
- Educational response with learning opportunities
- Assistance level indicator (🎓 GUIDED, 📚 EXPLAINED, etc.)
- Questions or explanations based on your configuration

### Test 2: Environment Variables Working
Ask Goose: *"What's my current mentor configuration?"*

**Expected Response:**
Mentor Mode should show your active configuration settings.

### Test 3: Different Assistance Levels
Try changing `DEFAULT_ASSISTANCE_LEVEL` and test with the same question to see different response styles.

## 🎨 Profile Templates

### 📚 Learning Profile
Perfect for dedicated learning sessions:
```yaml
toolkits:
  - name: "mentor"
    package: "goose-mentor-mode"
env:
  DEFAULT_ASSISTANCE_LEVEL: "guided"
  LEARNING_PHASE: "skill_building"
  TIMELINE_PRESSURE: "low"
  FORCE_MENTOR_MODE: "true"
  ENABLE_VALIDATION_CHECKPOINTS: "true"
  MAX_GUIDANCE_DEPTH: "5"
```

### ⚡ Production Profile
For when you need quick solutions:
```yaml
toolkits:
  - name: "developer"
  - name: "mentor"
    package: "goose-mentor-mode"
env:
  DEFAULT_ASSISTANCE_LEVEL: "automated"
  LEARNING_PHASE: "production"
  TIMELINE_PRESSURE: "high"
  ENABLE_VALIDATION_CHECKPOINTS: "false"
  MAX_GUIDANCE_DEPTH: "1"
```

### 🎯 Balanced Profile
Good all-around configuration:
```yaml
toolkits:
  - name: "developer"
  - name: "mentor"
    package: "goose-mentor-mode"
env:
  DEFAULT_ASSISTANCE_LEVEL: "explained"
  LEARNING_PHASE: "skill_building"
  TIMELINE_PRESSURE: "medium"
  ENABLE_VALIDATION_CHECKPOINTS: "true"
  MAX_GUIDANCE_DEPTH: "3"
```

## 🚨 Troubleshooting

### Issue: Mentor toolkit not found
**Symptoms:** Error like "toolkit 'mentor' not found"

**Solutions:**
1. Verify package installation: `pip show goose-mentor-mode`
2. Restart Goose Desktop after adding the toolkit
3. Check the package name is exactly: `goose-mentor-mode`

### Issue: No educational responses
**Symptoms:** Goose responds normally without mentor features

**Solutions:**
1. Check profile has `mentor` toolkit listed
2. Verify environment variables are set correctly
3. Try asking an educational question: *"How do I learn React?"*
4. Check for typos in environment variable names

### Issue: Too much/too little guidance
**Symptoms:** Responses don't match your preference

**Solutions:**
1. Adjust `DEFAULT_ASSISTANCE_LEVEL`:
   - Too much: Change to `assisted` or `automated`
   - Too little: Change to `explained` or `guided`
2. Modify `MAX_GUIDANCE_DEPTH` (1=minimal, 5=maximum)
3. Toggle `ENABLE_VALIDATION_CHECKPOINTS`

### Issue: Environment variables not working
**Symptoms:** Configuration doesn't affect responses

**Solutions:**
1. Ensure variables are in the Environment Variables section (not elsewhere)
2. Values should be strings: `"true"` not `true`
3. Restart Goose Desktop after changes
4. Check for typos in variable names

## 📞 Getting Help

If you're still having issues:

1. **Check the logs:** Look for error messages in Goose Desktop
2. **Test installation:** Run `python -c "import goose_mentor_mode; print('Working!')"`
3. **Reset configuration:** Try with a fresh profile
4. **Community support:** [GitHub Discussions](https://github.com/joeeuston-dev/goose-mentor-mode/discussions)

## 🎯 Quick Start Checklist

- [ ] Package installed with `pip install goose-mentor-mode`
- [ ] Toolkit added to profile: `mentor` (package: `goose-mentor-mode`)
- [ ] Environment variables configured (optional)
- [ ] Profile saved and selected
- [ ] Tested with an educational question
- [ ] Verified mentor features are working

---

**🎓 You're ready to transform your AI assistance into a learning experience!**
