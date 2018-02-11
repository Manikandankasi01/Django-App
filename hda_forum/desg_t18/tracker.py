import os
import xlrd
from datetime import datetime,timedelta
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
tracker_path=os.path.join(base_path,'templates','MasterTracker')

# m_tracker=pd.ExcelFile(tracker_path+"\\Master_Tracker_v8.6.xlsx")
# desg=pd.read_excel(tracker_path+"\\Master_Tracker_v8.6.xlsx",sheetname="DESG T18 Allocation")
#
master_tracker=xlrd.open_workbook(tracker_path+"\\Master_Tracker_v8.6.xlsx")

pdc=master_tracker.sheet_by_name("DESG PDC Allocation")
desg=master_tracker.sheet_by_name("DESG T18 Allocation")
ldm=master_tracker.sheet_by_name("LDM Allocation")
dsg_iab=master_tracker.sheet_by_name("DSG - IAB Allocation")
ndq_iab=master_tracker.sheet_by_name("NDQ - IAB Allocation")
dsg_fab=master_tracker.sheet_by_name("DSG - FAB Allocation")
ndq_fab=master_tracker.sheet_by_name("NDQ - FAB Allocation")
transit=master_tracker.sheet_by_name("Transit Allocation")

today=datetime.now()
print (today)
d = datetime.today() - timedelta(days=30)
print(d)

# desg_report()
# def desg_report():
for i in range(desg.nrows):
	input_date=desg.cell(i,7).value
	print(input_date)
	st=desg.cell(i,6).value
	status=st.strip()
	sam_name=desg.cell(i,0).value
	if type(input_date) == float:
		print (datetime.fromtimestamp(input_date))
		date=xlrd.xldate_as_tuple(desg.cell(i,7).value,master_tracker.datemode)
		#desg_input_date.append(date)
		print (type(date))
		if date < d:
			print (date)