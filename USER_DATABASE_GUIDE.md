# 🗂️ User Database System - Quick Reference

## Overview
Each user in the system has their own personalized profile displayed on their homepage. The system includes 5 pre-configured medical professionals.

---

## 🔑 Login Credentials

| User ID | Password | Name | Role | Department |
|---------|----------|------|------|-----------|
| doctor1 | mediflow2026 | Dr. John Doe | Consultant Physician | Internal Medicine |
| doctor2 | mediflow2026 | Dr. Sarah Smith | Head of Radiology | Radiology |
| doctor3 | mediflow2026 | Dr. Robert Chen | Internal Medicine Specialist | Internal Medicine |
| doctor4 | mediflow2026 | Dr. Lisa Patel | Senior Consultant Cardiologist | Cardiology |
| doctor5 | mediflow2026 | Dr. Michael Johnson | Laboratory Director | Laboratory Medicine |

---

## 📁 Database Structure

**File**: `users_database.json`

**Format**:
```json
{
  "users": [
    {
      "user_id": "doctor1",
      "password": "mediflow2026",
      "name": "Dr. John Doe",
      "email": "john.doe@hospital.local",
      "role": "Consultant Physician",
      "specialty": "Internal Medicine & Diagnostics",
      "department": "General Medicine",
      "bio": "...",
      "credentials": ["MD, Harvard Medical School", ...],
      "stats": {
        "consultations": "1,200+",
        "research_papers": "84",
        "patient_rating": "4.9/5"
      },
      "contact": {
        "office_phone": "+1-555-0123",
        "office_room": "302A",
        "office_hours": "Mon-Fri 9AM-5PM"
      },
      "avatar_url": "https://via.placeholder.com/140?text=Dr.+John+Doe"
    }
  ]
}
```

---

## 👤 User Profile Fields

Each user has the following fields:

| Field | Type | Example |
|-------|------|---------|
| user_id | String | "doctor1" |
| password | String | "mediflow2026" |
| name | String | "Dr. John Doe" |
| email | String | "john.doe@hospital.local" |
| role | String | "Consultant Physician" |
| specialty | String | "Internal Medicine & Diagnostics" |
| department | String | "General Medicine" |
| bio | String | Professional biography |
| credentials | Array | Medical degrees and certifications |
| stats.consultations | String | "1,200+" |
| stats.research_papers | String | "84" |
| stats.patient_rating | String | "4.9/5" |
| contact.office_phone | String | "+1-555-0123" |
| contact.office_room | String | "302A" |
| contact.office_hours | String | "Mon-Fri 9AM-5PM" |
| avatar_url | String | Image URL |

---

## 📋 New Features Added

### 1. Personalized Homepage
When users log in, they see:
- Welcome message with their name
- Professional profile card with photo
- Bio and complete about section
- Credentials and certifications
- Office contact information
- Statistics (consultations, publications, ratings)

### 2. Staff Directory Page
- Browse all medical professionals
- Search by name, specialty, or department
- Sort by Name, Department, or Specialty
- View quick profile cards
- Click to see full profile details

### 3. User Authentication Database
- Secure login with user credentials
- Dynamic profile loading
- Session-based user tracking

---

## 🚀 How to Use

### 1. Login with Different Users
```
Option 1 - Dr. John Doe (Consultant Physician)
  ID: doctor1
  Password: mediflow2026

Option 2 - Dr. Sarah Smith (Head of Radiology)
  ID: doctor2
  Password: mediflow2026

... and so on for doctor3, doctor4, doctor5
```

### 2. View Your Profile
After login:
- Go to 🏠 Homepage
- See your personalized profile section
- View your credentials and contact info

### 3. Browse Staff Directory
- Click 📋 Staff Directory on sidebar
- Search by name, specialty, or department
- View quick profiles or full profiles
- See all colleagues' information

---

## 🔧 Adding New Users

To add a new user to the database, edit `users_database.json`:

```json
{
  "user_id": "doctor6",
  "password": "mediflow2026",
  "name": "Dr. New User",
  "email": "new.user@hospital.local",
  "role": "Specialist",
  "specialty": "Your Specialty",
  "department": "Your Department",
  "bio": "Professional biography...",
  "credentials": ["MD", "Board Certified"],
  "stats": {
    "consultations": "500+",
    "research_papers": "20",
    "patient_rating": "4.7/5"
  },
  "contact": {
    "office_phone": "+1-555-0128",
    "office_room": "Room 123",
    "office_hours": "Mon-Fri 9AM-5PM"
  },
  "avatar_url": "https://via.placeholder.com/140?text=Dr.+Name"
}
```

---

## 💾 Database Features

✅ **Persistent Storage**: User data stored in JSON file
✅ **User-Specific**: Each user sees their own profile
✅ **Dynamic Loading**: Profiles loaded from database on login
✅ **Search & Filter**: Staff directory with multiple search options
✅ **Easy to Extend**: Simple JSON format, easy to add/edit users

---

## 🔐 Security Notes

This is a **demo/hackathon version**. For production:
- Encrypt passwords
- Use proper database (SQL, NoSQL)
- Implement role-based access control
- Add audit logging
- Use HTTPS for communication
- Implement 2FA if needed

---

## 📊 User Statistics

### Current Users: 5
- **Consultations**: 1,200+ to 5,000+
- **Research Papers**: 20 to 84
- **Patient Ratings**: 4.6/5 to 4.9/5

---

## 🎯 Navigation Guide

### After Login:


3. Review your professional information
4. See your contact details

### Workflow 2: Find a Colleague
1. Click 📋 Staff Directory
2. Search for department: "Cardiology"
3. Click colleague's profile
4. View full details including contact info

### Workflow 3: Browse All Staff
1. Go to Staff Directory
2. Sort by "Department"
3. Browse through all medical professionals
4. Click profiles to see details

---

## ❓ FAQ

**Q: Can I change my password?**
A: Currently passwords are stored in the JSON file. Edit `users_database.json` to change.

**Q: How do I add a new doctor?**
A: Edit `users_database.json` and add a new user object with all required fields.

**Q: Can multiple users login simultaneously?**
A: Yes, but each session is independent. Each browser session maintains separate state.

**Q: Where are passwords stored?**
A: In the `users_database.json` file (for demo purposes only).

**Q: Can users see other users' private data?**
A: Currently, the Staff Directory shows professional information. Private data not exposed.

---

## 🌟 Features

✨ **Personalized Homepages** - Each user sees their own profile
✨ **Staff Directory** - Browse all colleagues
✨ **Search & Filter** - Find staff by name, specialty, or department
✨ **Full Profiles** - View complete professional information
✨ **Contact Information** - Easy access to office details
✨ **Statistics Dashboard** - View professional metrics

---

**Version**: 1.0
**Last Updated**: March 11, 2026
**Status**: ✅ Ready to Use
