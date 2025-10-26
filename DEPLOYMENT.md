# Deployment Guide for Online Tutorial and Quiz System

This guide will walk you through deploying your Django application to Render.

## Prerequisites
- ✅ GitHub repository is ready: https://github.com/Shaaz29/Online-Tutorial-and-Quiz.git
- ✅ Code is pushed to GitHub
- ✅ Production-ready settings configured
- ✅ Build script and dependencies ready

---

## Step-by-Step Deployment Instructions

### Step 1: Create a Render Account
1. Go to [Render.com](https://render.com)
2. Click **"Get Started"** or **"Sign Up"**
3. Sign up with your GitHub account (recommended for easy integration)

### Step 2: Create a PostgreSQL Database
1. In your Render dashboard, click **"New +"** button
2. Select **"PostgreSQL"**
3. Configure the database:
   - **Name**: `online-tutorial-quiz-db`
   - **Database**: `online-tutorial-quiz-db`
   - **User**: `online-tutorial-quiz-db-user` (or auto-generated)
   - **Region**: Choose closest to you
   - **PostgreSQL Version**: 15
   - **Plan**: Select **Free** for testing
4. Click **"Create Database"**
5. **Copy the "Internal Database URL"** - you'll need this later

### Step 3: Create a Web Service
1. In Render dashboard, click **"New +"** button
2. Select **"Web Service"**
3. Connect your GitHub repository:
   - If you haven't connected GitHub, click **"Connect GitHub"** and authorize
   - Select your repository: `Shaaz29/Online-Tutorial-and-Quiz`
   - Choose the repository when it appears in the list

### Step 4: Configure Web Service Settings
In the "Create New Web Service" form, configure:

**Basic Settings:**
- **Name**: `online-tutorial-quiz-system`
- **Region**: Choose the same region as your database
- **Branch**: `master` (or `main` if that's your default branch)
- **Root Directory**: Leave empty (uses project root)

**Build Settings:**
- **Runtime**: `Python 3`
- **Build Command**: `chmod +x ./build.sh && ./build.sh`
- **Start Command**: `gunicorn online_tutorial_system.wsgi:application`

**Advanced Settings - Environment Variables:**
Add these environment variables:

| Key | Value | Description |
|-----|-------|-------------|
| `SECRET_KEY` | (Auto-generated) | Django secret key (Render will generate) |
| `DEBUG` | `False` | Disable debug mode in production |
| `DATABASE_URL` | (Your PostgreSQL Internal URL) | From Step 2 |
| `ALLOWED_HOSTS` | `your-app-name.onrender.com` | Your app URL (Render provides) |

**Important**: For `ALLOWED_HOSTS`, use this format:
```
your-app-name.onrender.com
```

Replace `your-app-name` with your actual app name that Render assigns.

### Step 5: Create Database (Optional with render.yaml)
If you're using the `render.yaml` file, you can skip manual database creation. The file will handle it automatically when deployed via the dashboard or CLI.

### Step 6: Deploy
1. Click **"Create Web Service"**
2. Render will start the deployment process
3. Watch the build logs - it should:
   - Install dependencies from `requirements.txt`
   - Run `collectstatic` to gather static files
   - Run migrations to set up the database
   - Start the Gunicorn server

### Step 7: Monitor Deployment
1. Watch the build logs in real-time
2. Look for messages like:
   - ✅ "Building application..."
   - ✅ "Installing dependencies..."
   - ✅ "Collecting static files..."
   - ✅ "Running migrations..."
   - ✅ "Build completed successfully!"

### Step 8: Access Your Application
1. Once deployment is complete, your app will be live at:
   ```
   https://your-app-name.onrender.com
   ```
2. The first load might take a few seconds (free tier "spins down" after inactivity)
3. Create a superuser to access the admin panel:
   - Open the Render Shell for your web service
   - Run: `python manage.py createsuperuser`

---

## Post-Deployment Tasks

### Create Superuser (Admin)
1. In Render dashboard, go to your web service
2. Click **"Shell"** tab
3. Run these commands:
   ```bash
   python manage.py createsuperuser
   ```
4. Follow prompts to create admin account

### Access Admin Panel
Visit: `https://your-app-name.onrender.com/admin/`

### Set Up Media Files (Optional)
If you need to upload images/files:
1. Go to **"Environment"** tab in Render
2. Add environment variable:
   - Key: `MEDIA_ROOT`
   - Value: `/opt/render/project/src/media`
3. Re-deploy the service

---

## Configuration Files Created

### Files for Production:
1. **build.sh** - Build script for Render
   - Installs dependencies
   - Collects static files
   - Runs migrations

2. **render.yaml** - Render configuration
   - Defines web service
   - Sets up PostgreSQL database
   - Configures environment variables

3. **requirements.txt** (updated)
   - Added: `whitenoise` for static files
   - Added: `dj-database-url` for database URL parsing
   - Added: `gunicorn` for production server

4. **settings.py** (updated)
   - Environment-based configuration
   - PostgreSQL support
   - Production settings

---

## Troubleshooting

### Build Fails
- Check build logs for specific errors
- Ensure all dependencies are in `requirements.txt`
- Verify Python version matches `runtime.txt`

### Static Files Not Loading
- Check if `collectstatic` ran successfully
- Verify `STATIC_ROOT` setting
- Check browser console for 404 errors

### Database Connection Error
- Verify `DATABASE_URL` environment variable is set correctly
- Check database is running (green status in Render dashboard)
- Ensure you're using the **Internal Database URL**

### App Returns 500 Error
- Check application logs in Render dashboard
- Verify `SECRET_KEY` is set
- Check `ALLOWED_HOSTS` includes your domain

### First Load is Slow
- Normal for free tier (spins down after 15 minutes of inactivity)
- Subsequent requests are faster

---

## Environment Variables Reference

| Variable | Required | Description | Example |
|----------|----------|-------------|---------|
| `SECRET_KEY` | Yes | Django secret key | Auto-generated |
| `DEBUG` | Yes | Debug mode | `False` |
| `DATABASE_URL` | Yes | PostgreSQL URL | Auto-provided |
| `ALLOWED_HOSTS` | Yes | Allowed domains | `yourapp.onrender.com` |
| `PYTHON_VERSION` | No | Python version | `3.12.12` |

---

## Free Tier Limitations

⚠️ **Important Notes:**
- Free tier apps "spin down" after 15 minutes of inactivity
- Free PostgreSQL databases are deleted after 90 days of inactivity
- Backup your database regularly
- Consider upgrading for production use

---

## Next Steps
1. ✅ Application deployed successfully
2. 🎯 Test all features (login, tutorials, quizzes)
3. 📊 Monitor application logs
4. 🔒 Update SECRET_KEY for security
5. 🚀 Consider custom domain setup

---

## Additional Resources
- [Render Documentation](https://render.com/docs)
- [Django on Render](https://render.com/docs/deploy-django)
- [Render PostgreSQL](https://render.com/docs/managed-postgres)

---

Good luck with your deployment! 🚀

