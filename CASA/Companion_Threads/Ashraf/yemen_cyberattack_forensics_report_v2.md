
# Digital Forensics Incident Report – Yemen Cyberattack (DNS Hijack + DDoS)

**Prepared by:** Ashraf Alhajj – Cybersecurity Expert  
**Date:** 24–25 July 2025  

---

## 1. Executive Overview

Between **24–25 July 2025**, YemenNet (AS30873) experienced a **coordinated, multi-vector cyberattack** involving:

- **DNS Hijacking** – Compromise of authoritative DNS servers for *.ye domains*, leading to **75+ defaced or offline websites**.  
- **Layer-7 DDoS (HTTP Floods)** – Attacks overwhelmed PPPoE/RADIUS authentication servers, causing **60% of ADSL users** to lose connectivity after modem restarts.

**Cloudflare Radar** confirmed an **11,000% surge** in Layer-7 malicious traffic during this incident.

---

## 2. Key Impacted Websites and Domains

### Government and Media
```
saba.ye              | Yemen News Agency (SABA)
customs.gov.ye       | Yemen Customs Authority
presidency.gov.ye    | Presidency of Yemen
yemenarmy.com        | Yemen Armed Forces
tvaden.net           | Aden TV
yemen-tv.net         | Yemen TV
yemenrtv.net         | Yemen Radio & TV
shebatv.net          | Sheba TV Network
topresidency.net     | Yemeni Presidency
yemen-media.gov.ye   | Yemen Media Government
```

### Educational
```
taiz.edu.ye          | Taiz University – جامعة تعز
academic.taiz.edu.ye | Academic Subdomain
elib.taiz.edu.ye     | e-Library
fe.taiz.edu.ye       | Faculty of Engineering
smartgate.edu.ye     | Smart Gate Portal
gti.edu.ye           | General Telecommunication Institute
```

### Financial and Telecom
```
onecash.com.ye       | OneCash – E-wallet
mtc.com.ye           | MTC Telecom
new.onecashye.com    | OneCash Service
speed-charge.com     | E-Payment Gateway
```

### Religious and Ministries
```
awqaf.gov.ye         | Ministry of Awqaf
haj.gov.ye           | Ministry of Hajj & Religious Affairs
mohesr.gov.ye        | Ministry of Higher Education
```

---

## 3. Attack Scenario (Kill Chain)

```
[Phase 1: Reconnaissance]
        |
        v
[Phase 2: Weaponization]
        |
        v
[Phase 3: Execution - DNS Hijack/Defacement]
        |
        v
[Phase 4: Diversion - Layer-7 DDoS]
        |
        v
[Phase 5: Public Claim - Telegram posts & propaganda]
```

---

## 4. Network Attack Flow Diagram

```
   [Attacker Botnets] 
          |
          v
   [L7 HTTP Flood] ---> [PPP/RADIUS Servers] ---> [ADSL Users]
          |
          v
   [DNS Hijack] ---> [ns1/ns2.yemen.net.ye]
                         |
                         v
           [Government & University Websites]
```

---

## 5. Forensic Timeline (24 July 2025 – UTC)

```
00:00–02:00   Early HTTP flood traffic observed.
03:30         Layer-7 spikes begin; WAF mitigation engaged.
07:30         Attack peaks (>11,000% surge) – DNS queries fail.
09:00–12:00   75+ websites defaced.
14:00         ADSL users report major outage (60% modems fail).
18:00+        DDoS persists; Telegram claims appear.
```

---

## 6. Technical Evidence

**Cloudflare Radar:**  
- **83.4%** of malicious traffic = Layer-7 DDoS.  
- **Top ASN:** AS30873 (YemenNet) = **95.9%** of attack traffic.  
- **Traffic Origin:** US, EG, FR, NL, SG, etc.  
- **Spike:** +11,000% increase in L7 attack volume at 07:30 UTC.

**DNS Forensics:**  
- SOA serial changes on `saba.ye`, `customs.gov.ye`.  
- No **DNSSEC**, enabling hijack via record tampering.

**Defacement Proof:**  
- Banners: **“Hacked by S4uD1Pwnz”** on affected domains.

---

## 7. Root Cause Analysis

- **Centralized DNS infrastructure** (single NS) with no DNSSEC.  
- **Lack of DDoS mitigation** on PPPoE and DNS control planes.  
- **Weak security controls** for DNS admin panels (possible credential leaks).

---

## 8. Recommendations

### Immediate (0–7 Days)
- Activate **DNSSEC** for *.ye.  
- Restore DNS zones from clean backups.  
- Deploy **Cloudflare Magic Transit / Radware DDoS defense**.

### Short-Term (7–30 Days)
- Add **secondary DNS servers (multi-cloud)**.  
- Apply **Registry Lock** to prevent unauthorized zone edits.  
- Geo-distribute PPPoE/RADIUS servers.

### Long-Term (1–3 Months)
- Implement **continuous BGP/DNS monitoring** with alerting (BGPalerter, RIPE RIS).  
- Conduct **red-team DNS/infra assessments**.  
- Establish a **national CERT for Yemen**.

---

## 9. Lessons Learned
1. **Single Point of Failure:** Centralized DNS is a national risk.  
2. **DNSSEC is essential:** Prevents record tampering.  
3. **L7 DDoS needs advanced defense:** Traditional firewalls fail under HTTP floods.  
4. **Preparedness:** Pre-defined Incident Response reduces downtime.  
5. **Monitoring:** Real-time detection of anomalies is critical.

---

## 10. References
- [Cloudflare Radar – Yemen](https://radar.cloudflare.com/ye)  
- Telegram posts by **S4uD1Pwnz** (screenshots archived).  
- Defacement artifacts (`swslc-yemen.com.ye`).

---
