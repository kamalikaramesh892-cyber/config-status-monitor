# Test Cases — Configuration Audit System

## TC01 — Audit Log Display
- **Test:** Open website and check audit log table
- **Expected:** All commits shown with author, date, message
- **Result:** PASS ✅

## TC02 — Python Script Generation
- **Test:** Run python generate_log.py
- **Expected:** git_log.json created with real commit data
- **Result:** PASS ✅

## TC03 — Search Functionality
- **Test:** Type author name in search box
- **Expected:** Only that author's commits shown
- **Result:** PASS ✅

## TC04 — Filter by Author
- **Test:** Select author from dropdown
- **Expected:** Table filters correctly
- **Result:** PASS ✅

## TC05 — Status Accounting
- **Test:** Check status table for all files
- **Expected:** All files show correct version and CI type
- **Result:** PASS ✅

## TC06 — Multiple Contributors
- **Test:** Check contributors section
- **Expected:** Both Kamali and Yuvashree shown with commit count
- **Result:** PASS ✅

## TC07 — FCA Audit Results
- **Test:** Check FCA section
- **Expected:** All files show PASS status
- **Result:** PASS ✅

## TC08 — Responsive Design
- **Test:** Open website on mobile screen
- **Expected:** Layout adjusts properly
- **Result:** PASS ✅