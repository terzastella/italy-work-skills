# impegnativa-visite cases

## Good: knee MRI, class D

Input: GP referral class D [sample data].

Output: wait logic (class + CUP) + booking steps + ticket check +
`wrong class suspected? Ask GP to fix — stated as action.`

## Bad: class accepted blindly

Input: "tanto aspetto comunque mesi" with wrong class suspected [sample data].

Output: `Wrong class suspected? Ask GP to fix first — waiting on a wrong class wastes months. Stated as action.`
