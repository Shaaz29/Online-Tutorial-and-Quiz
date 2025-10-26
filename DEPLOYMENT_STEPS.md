# Complete Deployment Steps for Render

## ✅ Step 1: Database Created
Your PostgreSQL database is ready!

---

## 🚀 Step 2: Create Web Service

### In Render Dashboard:
1. Click **"New +"** button (top right)
2. Select **"Web Service"**

### Connect GitHub Repository:
1. If not connected, click **"Connect GitHub"** and authorize Render
2. Search for: `Shaaz29/Online-Tutorial-and-Quiz`
3. Click on the repository

---

## ⚙️ Step 3: Configure Web Service Settings

### Basic Settings Tab:
```
Name: online-tutorial-quiz-system
Region: Oregon (US West)  (or same as your database)
Branch: master
Root Directory: (leave empty)
```

### Build Settings Tab:
```
Runtime: Python 3
Build Command: chmod +x ./build.sh && ./build.sh
Start Command: gunicorn online_tutorial_system.wsgi:application
```

### Environment Tab - Click "Add Environment Variable" for each:

**1. SECRET_KEY**
```
Key: SECRET_KEY
Value: EwCeyoQDyUPKqv7H4JB260quwyJ8XGLWYGgeXGwgJxvihZ_hpm7OIcPK0UCWjBhHqQY
```

**2. DEBUG**
```
Key: DEBUG
Value: False
```

**3. DATABASE_URL**
```
Key: DATABASE_URL
Value: postgresql://online_tutorial_quiz_db_user:mV7N6tyM5u4gFSTdh1e0j6qThkoJTr94@dpg-d3v0j2pr0fns73c50h9g-a/online_tutorial_quiz_db
```

**4. ALLOWED_HOSTS**
```
Key: ALLOWED_HOSTS
Value: (Leave this empty initially)
```
*Note: After deployment, Render will provide your app URL. You may need to add it here.*

---

## 🎯 Step 4: Deploy

1. Review all settings
2. Scroll down and click **"Create Web Service"**
3. Wait for deployment to complete (5-10 minutes)

---

## 📊 Step 5: Monitor Build

Watch the logs for these success messages:
```
✅ Building application...
✅ Installing dependencies...
✅ Collecting static files...
✅ Running migrations...
✅ Build completed successfully!
```

---

## 👤 Step 6: Create Superuser

Once deployed, create an admin account:

1. In Render dashboard, go to your web service
2. Click on **"Shell"** tab
3. Run this command:
   ```bash
   python manage.py createsuperuser
   ```
4. Follow prompts:
   - Username: (your choice)
   - Email: (your email)
   - Password: (your password)

---

## 🌐 Step 7: Access Your Application

Your app will be live at:
```
https://your-app-name.onrender.com
```

Admin panel:
```
https://your-app-name.onrender.com/admin/
```

---

## 🔄 Step 8: Update ALLOWED_HOSTS (If needed)

After deployment, if you see a "DisallowedHost" error:

1. Go to your web service dashboard
2. Click **"Environment"** tab
3. Find the `ALLOWED_HOSTS` variable
4. Add your app URL (without https://):
   ```
   your-app-name.onrender.com
   ```
5. Click **"Save Changes"**
6. Service will auto-redeploy

---

## ⚠️ Important Notes

1. **First load is slow** - Free tier apps spin down after 15 minutes of inactivity
2. **Database backups** - Free databases are deleted after 90 days of inactivity
3. **Environment variables** - Keep your SECRET_KEY and DATABASE_URL secure
4. **Static files** - Should collect automatically during build

---

## 📋 Quick Reference Card

**Database Details:**
- Name: `online_tutorial_quiz_db`
- User: `online_tutorial_quiz_db_user`
- Host: `dpg-d3v0j2pr0fns73c50h9g-a`

**Environment Variables:**
```
SECRET_KEY=EwCeyoQDyUPKqv7H4JB260quwyJ8XGLWYGgeXGwgJxvihZ_hpm7OIcPK0UCWjBhHqQY
DEBUG=False
DATABASE_URL=postgresql://online_tutorial_quiz_db_user:mV7N6tyM5u4gFSTdh1e0j6qThkoJTr94@dpg-d3v0j2pr0fns73c50h9g-a/online_tutorial_quiz_db
```

**Build Commands:**
- Build: `chmod +x ./build.sh && ./build.sh`
- Start: `gunicorn online_tutorial_system.wsgi:application`

---

## 🆘 Troubleshooting

**Build fails?**
- Check build logs for specific errors
- Verify all environment variables are set
- Ensure DATABASE_URL is the Internal URL

**Database connection error?**
- Verify DATABASE_URL is correct (use Internal URL)
- Check database is running (green status)
- Ensure no extra spaces in environment variables

**500 error?**
- Check application logs
- Verify SECRET_KEY is set
- Check ALLOWED_HOSTS includes your domain

---

Good luck! 🚀

