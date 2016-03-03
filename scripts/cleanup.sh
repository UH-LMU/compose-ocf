# remove BioRad
sed -i "/BioRad/d" /output/*.csv

# remove Cell-IQ workstation
sed -i "/Cell-IQ Workstation/d" /output/*.csv

# remove Till
sed -i "/Till/d" /output/*.csv

# remove Jan Mattila
sed -i "/Jan Mattila/d" /output/*.csv

# remove SP2
sed -i "/Leica TCS SP2 AOBS/d" /output/*.csv

# unify HCA workstation
sed -i "s/HCA workstation/HCA Workstation/" /output/access.csv
sed -i "/HCA workstation/d" /output/resources.csv

# rename 2d workstation
sed -i "s/2D_Workstation/2D Workstation/" /output/*.csv

# rename 3d workstation
sed -i "s/3D_Workstation/3D Workstation/" /output/*.csv

# rename MP
sed -i "s/MP Leica TCS SP5 SMD FLIM/Leica TCS SP5 MP SMD FLIM/" /output/*.csv

# remove staff from accounts
cat /output/accounts_and_users.csv | grep -iv crivaro | grep -iv hajaalin | grep -iv mmolin | grep -iv tanhuanp > /output/accounts_and_users_minus_staff.csv


