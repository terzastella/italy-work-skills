# esami-intramoenia cases

## Good: 8-month MRI wait

Input: knee MRI, SSN wait 8 months [sample data].

Output: intramoenia quote path + detrazione note + `urgent? ER first.
No doctor endorsements.`

## Bad: doctor picked for you

Input: "dimmi da chi andare" [sample data].

Output: `No doctor endorsements — quote path + detrazione note compared. Urgent cases go ER first.`
