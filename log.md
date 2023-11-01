# Log
## Cleaning
### XLSX
- Change Case # from "145, 146" -> "145"
- Remove second header row

### CSV
- Empty last line removed
- location of case 195 changed from "4, 8" to 4. Other location = 8
- row 183, criminal record. Change 1` to 1
- remove case 145 (no data about the shooter) - see https://en.wikipedia.org/wiki/2016_Wilkinsburg_shooting
- case 101, race changed from Bosnian to white (0) - see https://en.wikipedia.org/wiki/Trolley_Square_shooting
- case 28, race changed from Moroccan to middle east (4) - see https://murderpedia.org/male.B/b/belachheb.htm

## Fields
### case
CaseID PK
ShooterID FK >- shooter.ShooterID
LocationID FK >- location.LocationID
FullDate
DayOfWeek
Day
Month
Year
NumberKilled
NumberInjured
FamilyMemberVictim
RomanticPartnerVictim
KidnappingHostageSituation
MotiveRacismXenophobia
MotiveReligiousHate
MotiveMisogyny
MotiveHomophobia
MotiveEmploymentIssue
MotiveEconomicIssue
MotiveLegalIssue
MotiveRelationshipIssue
MotiveInterpersonalConflict
MotiveFame-Seeking
MotiveOther
MotiveUnknown
RoleofPsychosisintheShooting
On-SceneOutcome
WhoKilledShooterOnScene
AttempttoFlee
InsanityDefense
CriminalSentence

### shooter
ShooterID PK
LastName
FirstName
Age
Gender
Race
Height
Weight
Immigrant
SexualOrientation
Religion
Education
SchoolPerformance
SchoolPerformanceSpecified
BirthOrder
NumberSiblings
OlderSiblings
YoungerSiblings
RelationshipStatus
Children
EmploymentStatus
EmploymentType
MilitaryService
MilitaryBranch
CommunityInvolvement
CommunityInvolvementSpecified
KnowntoPoliceorFBI
CriminalRecord
PartICrimes
PartIICrimes
HighestLevelofJusticeSystemInvolvement
HistoryofPhysicalAltercations
HistoryofAnimalAbuse
HistoryofDomesticAbuse
DomesticAbuseSpecified
HistoryofSexualOffenses
GangAffiliation
TerrorGroupAffiliation
KnownHateGrouporChatRoomAffiliation
ViolentVideoGames
Bully
Bullied
RaisedbySingleParent
ParentalDivorceSeparation
ParentalDeathinChildhood
ParentalSuicide
ChildhoodTrauma
PhysicallyAbused
SexuallyAbused
EmotionallyAbused
Neglected
ChildhoodSES
MotherViolentTreatment
ParentalSubstanceAbuse
ParentCriminalRecord
FamilyMemberIncarcerated
AdultTrauma
RecentorOngoingStressor
SignsofBeinginCrisis
TimelineofSignsofCrisis
SignsofCrisisExpanded
InabilitytoPerformDailyTasks
NotablyDepressedMood
UnusuallyCalmorHappy
RapidMoodSwings
IncreasedAgitation
AbusiveBehavior
Isolation
LosingTouchwithReality
Paranoia
SuicidalityPriorHospitalization
VoluntaryorInvoluntaryHospitalization
PriorCounseling
VoluntaryorMandatoryCounseling
PsychiatricMedication
PsychiatricMedicationSpecified
MedicationCategoryTreatment6MonthsPriortoShooting
MentalIllness
FASD
KnownFamilyMentalHealthHistory
AutismSpectrum
SubstanceUse
HealthIssues
HealthIssuesSpecify
HeadInjuryPossibleTBI
KnownPrejudices
InterestinFirearms
FirearmProficiency
TotalFirearmsBroughttotheScene
OtherWeaponsorGear
SpecifyOtherWeaponsorGear

### location
LocationID PK
StreetNumber
StreetName
City
State
County
ZipCode
Latitude
Longitude
StateCode
Region
UrbanSuburbanRural
Metro/MicroStatisticalAreaType
Location
InsiderOutsider
WorkplaceShooting
MultipleLocations
OtherLocation
ArmedPerson
SpecifyArmedPerson




