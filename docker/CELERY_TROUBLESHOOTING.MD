# Airflow 3.x CeleryExecutor Troubleshooting Guides

This folder contains comprehensive guides for resolving common Airflow 3.x issues with CeleryExecutor in Docker Compose.

## 📚 Available Guides

### 1. **COMPLETE_ERROR_GUIDE.md** ⭐ START HERE
The complete story of how we resolved your issue, step-by-step.

**Includes:**
- All three errors you encountered (in order)
- Detailed explanation of each error
- Why each error happened
- Step-by-step resolution process
- Full explanations of Airflow 3.x architecture
- The debugging journey from symptom to solution

**Best for:** Understanding the complete troubleshooting process and learning how to debug similar issues.

### 2. **QUICK_FIX.md**
Get your Airflow working in 2 minutes.

**Includes:**
- The exact two fixes needed
- Copy-paste commands
- Minimal explanation
- Verification steps

**Best for:** Quick resolution when you just want it to work NOW.

### 3. **FIX_FERNET_KEY.md**
Deep dive into the Fernet key authentication error.

**Includes:**
- What Fernet keys are and why they matter
- How to generate them properly
- Security best practices
- Troubleshooting auth failures

**Best for:** Understanding authentication in Airflow 3.x.

### 4. **FIX_APISERVER_CONNECTION_ERROR.md**
Deep dive into the API Server connection error.

**Includes:**
- Airflow 3.x architecture changes
- Why API Server URL is required
- Docker networking explanation
- Connection troubleshooting

**Best for:** Understanding the new Airflow 3.x architecture.

### 5. **TROUBLESHOOTING_CELERY_STATE_MISMATCH.md**
Comprehensive troubleshooting guide with all possible solutions.

**Includes:**
- 12 detailed troubleshooting steps
- Database connection pool optimization
- Redis configuration
- Resource monitoring
- Advanced debugging techniques

**Best for:** When the quick fixes don't work and you need deeper troubleshooting.

---

## 🚀 Quick Start

### If you're seeing this error:
```
Executor CeleryExecutor reported that the task instance finished with state failed, 
but the task instance's state attribute is queued
```

### Do this:

1. **Read COMPLETE_ERROR_GUIDE.md** for the full story (recommended)
   - OR -
2. **Read QUICK_FIX.md** and apply the two fixes (fastest)

Both will get you to the same solution, just different paths!

---

## 🎯 The Two Fixes You Need

For 90% of Airflow 3.x cases:

```bash
# Fix #1: Add API Server URL to docker-compose.yaml
AIRFLOW__CORE__EXECUTION_API_SERVER_URL: 'http://airflow-apiserver:8080/execution/'

# Fix #2: Generate and add Fernet Key
docker-compose run --rm airflow-worker python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
# Copy output to docker-compose.yaml:
AIRFLOW__CORE__FERNET_KEY: 'YOUR_GENERATED_KEY'

# Restart
docker-compose down && docker-compose up -d
```

---

## 📖 Recommended Reading Order

**For Learners:**
1. COMPLETE_ERROR_GUIDE.md (understand everything)
2. TROUBLESHOOTING_CELERY_STATE_MISMATCH.md (advanced techniques)

**For Quick Fixes:**
1. QUICK_FIX.md (solve it now)
2. COMPLETE_ERROR_GUIDE.md (understand what you fixed)

**For Specific Errors:**
- Connection refused → FIX_APISERVER_CONNECTION_ERROR.md
- Auth token failed → FIX_FERNET_KEY.md
- Still broken → TROUBLESHOOTING_CELERY_STATE_MISMATCH.md

---

## 🤔 Which Guide Should I Read?

**"I want to understand what happened"**
→ COMPLETE_ERROR_GUIDE.md

**"Just make it work, I'm busy"**
→ QUICK_FIX.md

**"I see 'Connection refused'"**
→ FIX_APISERVER_CONNECTION_ERROR.md

**"I see 'Invalid auth token'"**
→ FIX_FERNET_KEY.md

**"Nothing works, help!"**
→ TROUBLESHOOTING_CELERY_STATE_MISMATCH.md

---

## 📝 Error Sequence

These errors appear in order:

```
Error #1: State Mismatch (symptom)
    ↓
Error #2: Connection Refused (root cause #1)
    ↓ Fix: Add API Server URL
    ↓
Error #3: Auth Token Failed (root cause #2)
    ↓ Fix: Add Fernet Key
    ↓
✅ SUCCESS!
```

---

## 💡 Key Concepts

### Airflow 3.x Architecture
- Workers communicate via **API Server** (new in 3.x)
- Requires **EXECUTION_API_SERVER_URL** configuration
- Different from Airflow 2.x (direct database access)

### Fernet Key
- Used for **internal authentication** between components
- **Encrypts/decrypts** auth tokens
- All containers must use the **same key**

### Docker Networking
- Container names become **hostnames**
- Automatic **DNS resolution** between containers
- No need for IP addresses

---

## ✅ Verification Checklist

After applying fixes:

- [ ] API Server URL configured in docker-compose.yaml
- [ ] Fernet Key generated and configured
- [ ] Services restarted: `docker-compose down && docker-compose up -d`
- [ ] All containers healthy: `docker-compose ps`
- [ ] Worker can reach API Server: `docker-compose exec airflow-worker curl http://airflow-apiserver:8080/execution/health`
- [ ] Fernet key set in worker: `docker-compose exec airflow-worker env | grep FERNET_KEY`
- [ ] DAG triggered and runs successfully
- [ ] No more "Connection refused" or "Auth token" errors in logs

---

## 🆘 Still Having Issues?

1. Check all services are healthy: `docker-compose ps`
2. Check worker logs: `docker-compose logs --tail=100 airflow-worker`
3. Check API server logs: `docker-compose logs --tail=100 airflow-apiserver`
4. Verify connectivity: `docker-compose exec airflow-worker curl http://airflow-apiserver:8080/execution/health`
5. Verify Fernet key matches across all services
6. Try the full troubleshooting guide: TROUBLESHOOTING_CELERY_STATE_MISMATCH.md

---

## 🎉 Success Indicators

You'll know it's working when:
- Tasks transition: queued → running → success
- Worker logs show "Marking task as SUCCESS"
- No error messages in worker logs
- DAG runs complete successfully
- Task instances show correct states in UI

---

**Happy Airflowing! 🚀**