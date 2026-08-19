"""Demo data generator for Murder Game - creates sample evidence files for testing."""

import os
from pathlib import Path

def create_demo_files():
    """Create demo evidence files for game testing."""
    
    # Create Admin_files
    admin_dir = Path("Admin_files")
    admin_dir.mkdir(exist_ok=True)
    
    # Create Player directory
    player_dir = Path("Player")
    player_dir.mkdir(exist_ok=True)
    
    # Create Files directory
    files_dir = Path("Files")
    files_dir.mkdir(exist_ok=True)
    
    print("🎮 Creating murder game demo files...\n")
    
    # ADMIN FILES - Case records
    print("Creating admin files...")
    
    admin_case_record = admin_dir / "case_record.txt"
    if not admin_case_record.exists():
        with open(admin_case_record, 'w') as f:
            f.write("""CASE #2026-08-19-001: MURDER INVESTIGATION
================================================

Victim: James Richardson (Age 45, CEO of Richardson Industries)
Location: Downtown Office, Building A, Floor 12
Time of Death: Between 11:00 PM - 1:00 AM
Discovered: 8:00 AM by cleaning staff

INITIAL FINDINGS:
- No signs of forced entry
- Victim was at desk, apparent blunt force trauma
- Safe in office was open but contents intact
- Personal documents scattered on floor

SUSPECTS UNDER INVESTIGATION:
1. Alice Morrison - Secretary (Works closest to victim)
2. Robert Chen - Business partner (Recent disputes over merger)
3. David Patel - Security guard (Had access to building)
4. Emma Wilson - Receptionist (Last person to see victim alive)

NEXT STEPS:
- Interview all suspects
- Examine alibis for critical time window
- Analyze financial records
- Check security camera footage

Case Status: ACTIVE INVESTIGATION
""")
        print(f"  ✓ Created {admin_case_record}")
    
    admin_suspects = admin_dir / "suspect_alibis.txt"
    if not admin_suspects.exists():
        with open(admin_suspects, 'w') as f:
            f.write("""SUSPECT ALIBIS - VERIFICATION STATUS
====================================

SUSPECT 1: Alice Morrison (Secretary)
Claimed Alibi: Was at home alone, watching Netflix
Verification: ⚠️ UNVERIFIED (lives alone, no witnesses)
Phone Records: Active in building until 10:47 PM
Notes: Has access to office keys, familiar with schedule

SUSPECT 2: Robert Chen (Business Partner)
Claimed Alibi: Was at airport lounge heading to SF
Verification: ✓ CONFIRMED (airport security footage, ticket purchase)
Phone Records: Turned off phone at 10:15 PM (during flight)
Notes: Was aware of victim's large life insurance policy

SUSPECT 3: David Patel (Security Guard)
Claimed Alibi: Was doing night patrol, rounds logged
Verification: ⚠️ PARTIALLY VERIFIED (patrol logs exist but no witnesses)
Phone Records: Inactive all night (duty protocol)
Notes: Had master keys to all rooms, no overtime requests logged

SUSPECT 4: Emma Wilson (Receptionist)
Claimed Alibi: Left work at 6:00 PM, went to dinner with friend
Verification: ✓ CONFIRMED (friend's statement, credit card receipt)
Phone Records: Normal activity, left building at 6:05 PM
Notes: May have seen something before leaving

PRIORITY LEADS:
1. Security camera footage from 10:00 PM - 1:00 AM
2. Financial records - insurance policy, will, debts
3. Office access logs from security system
4. Phone location data from night of incident
""")
        print(f"  ✓ Created {admin_suspects}")
    
    # PLAYER FILES - Evidence
    print("\nCreating player evidence files...")
    
    player_evidence = player_dir / "evidence_log.txt"
    if not player_evidence.exists():
        with open(player_evidence, 'w') as f:
            f.write("""EVIDENCE COLLECTED
==================

ITEM 1: Handwritten Note (Found in victim's desk drawer)
Content: "Meeting at midnight. Come alone. Back entrance."
Analysis: Written in recent ink, not victim's handwriting
Found: Desk drawer, third compartment
Evidence #: EV-001

ITEM 2: Security Badge (Found under victim's desk)
Badge ID: SG-42 (Security Guard - David Patel)
Condition: Slightly damaged, as if torn off hastily
Significance: Should be worn by guard at all times
Evidence #: EV-002

ITEM 3: Torn Receipt (Found in office trash)
Source: Local hardware store, purchase #5847
Time: 8:47 PM day of murder
Items: "Rope 50ft, Gloves, Flashlight"
Buyer: Unknown (cash purchase, no receipt name)
Evidence #: EV-003

ITEM 4: Video Footage (Building security cameras, 10:30 PM - 1:00 AM)
Status: [ENCRYPTED - See encrypted_footage.bmp]
Note: Critical footage shows hallway and office entrance
Evidence #: EV-004

NEXT ACTIONS:
- Identify who wrote the meeting note
- Determine if David Patel was in building
- Trace hardware store purchase
- Decrypt video footage for conclusive evidence
""")
        print(f"  ✓ Created {player_evidence}")
    
    # FILES - Clues and hints
    print("\nCreating game files...")
    
    game_victims = files_dir / "victim_background.txt"
    if not game_victims.exists():
        with open(game_victims, 'w') as f:
            f.write("""VICTIM PROFILE: James Richardson
================================

PERSONAL:
- Age: 45, Married (Wife: Catherine Richardson)
- Children: 2 (College-aged)
- Residence: Upscale apartment downtown
- Hobbies: Golf, wine collecting

PROFESSIONAL:
- Title: CEO, Richardson Industries (Manufacturing)
- Years in role: 12 years
- Company status: Profitable, recent $50M merger negotiations
- Salary: $500K + bonus
- Life Insurance: $2M policy (beneficiary: wife)

RECENT EVENTS:
- Merger talks with Chen Industries hit roadblock (1 week ago)
- Fired CFO (3 weeks ago) for financial irregularities
- Complained about "threats" to secretary (2 days ago)
- Requested security increase (1 day ago) - DENIED by board

FINANCIAL STATUS:
- Net worth: ~$15M
- Recent large cash withdrawals noted
- Some debt holdings in private accounts
- Will to be read shows unexpected provisions

RELATIONSHIPS:
- Wife: Stable marriage (30 years)
- Business partner Robert: Tense lately
- Employees: Generally well-liked but strict manager
- Security: Frequent conflicts with head of security

RED FLAGS:
- Why the cash withdrawals?
- Who made the midnight meeting request?
- Why increase security if not expecting danger?
""")
        print(f"  ✓ Created {game_victims}")
    
    print("\n✓ Demo files created successfully!")
    print("\nYou can now:")
    print("  1. Run: python main.py")
    print("  2. Use commands: list, open <file>, decode <file>")
    print("  3. Solve the mystery by reading evidence and examining clues!")
    print("\nExample commands:")
    print("  > open evidence_log.txt")
    print("  > open suspect_alibis.txt")
    print("  > decode encrypted_footage.bmp")

if __name__ == "__main__":
    create_demo_files()
