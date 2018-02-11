import os
import xlrd
from datetime import datetime
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

today=datetime.now().month

#1st month
one_pc_in_queue=[]
one_pc_inprogress=[]
one_pc_on_hold=[]
one_pc_completed=[]
one_pc_rejected=[]
one_gml_in_queue=[]
one_gml_inprogress=[]
one_gml_on_hold=[]
one_gml_completed=[]
one_gml_rejected=[]

#2nd month
two_pc_in_queue=[]
two_pc_inprogress=[]
two_pc_on_hold=[]
two_pc_completed=[]
two_pc_rejected=[]
two_gml_in_queue=[]
two_gml_inprogress=[]
two_gml_on_hold=[]
two_gml_completed=[]
two_gml_rejected=[]

#PDC
pdc_inprogress_status=["In Progress - PDC","In Progress - AFR Load","QA Completed - Ready for submission","In Progress-Delta","Delta completed-Ready for submission",]
pdc_queue_status=["In Queue - To be Assigned",]
pdc_completed_status=["PDC completed & AFR Submitted","AFR Load Completed & Posted","Delta completed & AFR submitted",]
pdc_on_hold_status=["On Hold",]
pdc_rejected_status=["Rejected",]
# # PC Status
# pc_inprogress_status=["In Progress - [PC] Perform Validation of T18","In Progress - [PC] Load PNI",]
# pc_queue_status=["In Queue - [PC] To be Assigned",]
# pc_completed_status=["Completed [PC] - Trigger Triage","Completed - [PC] GDSS Notification","On Hold - Paused in Triage",]
# pc_on_hold_status=["On Hold - Awaiting Address File","On Hold - [PC] Data Issues","On Hold - [PC] NDD not available","On Hold - [PC] Awaiting Boundary Update","On Hold - [PC] Issues - NBN Internal","On Hold - [PC] GDSS/PNI Issue",]
# pc_rejected_status=["Rejected - [PC] Sent Back to Telstra (DESG)","Rejected - [PC] Sent Back to Telstra (LDM)","Rejected - [PC] Sent Back to Telstra (AP)","Rejected - [PC] Sent Back to Telstra (Design/NA)"]
# # GML Status
# gml_queue_status=["In Queue - [GML] To be Assigned",]
# gml_inprogress_status=["In Progress - [GML] PNI Load - Complete Run","In Progress - [GML] Generate Trace Report",]
# gml_on_hold_status=["On Hold - [GML] Issues - NBN Internal","On Hold - [GML] PNI Issue","On Hold - [GML] Awaiting Boundary Update",]
# gml_rejected_status=["Rejected - [GML] Sent Back to Telstra (DESG)",]
# gml_completed_status=["Completed - [GML] Handover to DSG",]
# #LDM Status
# ldm_inprogress_status=["In Progress - LocID Matching","In Progress - LocID Matching Completed","In Progress - Repurposing","In Progress - Repurposing Completed","In Progress - Address Alignment","In Progress - Address Alignment Completed","In Progress - Final Validations",]
# ldm_queue_status=["In Queue - To be Assigned",]
# ldm_completed_status=["Completed - Handover done",]
# ldm_on_hold_status=["On Hold",]
# ldm_rejected_status=["Rejected",]
#IAB DSG
dsg_iab_inprogress_status=["In Progress","In Progress - HFC Completed",]
dsg_iab_queue_status=["In Queue - To be Assigned","In Queue - HFC Completed",]
dsg_iab_completed_status=["Completed",]
dsg_iab_on_hold_status=["On Hold - HFC Completed","On Hold - PNI Issues","On Hold - Data Issues","On Hold - Document Unavailability","On Hold - Awaiting Upstream team Updates","On Hold - PNI Issues","On Hold - Data Issues","On Hold - Document Unavailability","On Hold - Awaiting Upstream team Updates",]
dsg_iab_rejected_status=["Rejected",]
#IAB NDQ
ndq_iab_inprogress_status=["In Progress",]
ndq_iab_queue_status=["In Queue - To be Assigned (QI)","In Queue - To be Assigned (Defect Resolution)",]
ndq_iab_completed_status=["Completed","Completed - Handed over to NEO",]
ndq_iab_on_hold_status=["On Hold",]
ndq_iab_rejected_status=["Rejected",]
#FAB DSG
dsg_fab_inprogress_status=["In Progress",]
dsg_fab_queue_status=["In Queue - To be Assigned","In Queue - Awaiting T18 Lite",]
dsg_fab_completed_status=["Completed",]
dsg_fab_on_hold_status=["On Hold",]
dsg_fab_rejected_status=["Rejected",]
#FAB NDQ
ndq_fab_inprogress_status=["In Progress",]
ndq_fab_queue_status=["In Queue - To be Assigned (QI)","In Queue - To be Assigned (Defect Resolution)",]
ndq_fab_completed_status=["Completed - Handed over to NEO","Completed - Awaiting final Acceptance","Completed - Accepted by NEO",]
ndq_fab_on_hold_status=["On Hold",]
ndq_fab_rejected_status=["Rejected",]
#Transit
pc_inprogress_status=["In Progress - PNI Load","In Progress - Asset Remediation","In Progress - Defect Fix",]
pc_queue_status=["In Queue - To be Assigned (PNI Load)","In Queue - To be Assigned (Defects)",]
pc_completed_status=["Completed - Handed over to NDQ","Completed - Defects fixed & notified NDQ","Completed - Final Acceptance Received",]

def desg_report():
	one_pc_count=two_pc_count=third_pc_count=one_gml_count=two_gml_count=third_gml_count=[]
	for i in range(desg.nrows):
		input_date=desg.cell(i,7).value
		st=desg.cell(i,6).value
		status=st.strip()
		sam_name=desg.cell(i,0).value
		if type(input_date) == float:
			date=xlrd.xldate_as_tuple(desg.cell(i,7).value,master_tracker.datemode)
			date=datetime(*date[0:6])
			diff=today-date
			if diff.days>=9:
				if "Queue" in status and "PC" in status:
					one_pc_in_queue.append(sam_name)
				elif "In Progress" in status and "PC" in status:
					one_pc_inprogress.append(sam_name)
				elif "On Hold" in status and "PC" in status:
					one_pc_on_hold.append(sam_name)
				elif "Rejected" in status and "PC" in status:
					one_pc_rejected.append(sam_name)
				elif "Completed" in status and "PC" in status:
					one_pc_completed.append(sam_name)
				elif "Queue" in status and "GML" in status:
					one_gml_in_queue.append(sam_name)
				elif "In Progress" in status and "GML" in status:
					one_gml_inprogress.append(sam_name)
				elif "On Hold" in status and "GML" in status:
					one_gml_on_hold.append(sam_name)
				elif "Rejected" in status and "GML" in status:
					one_gml_rejected.append(sam_name)
				elif "Completed" in status and "GML" in status:
					one_gml_completed.append(sam_name)


			if diff.days>=30:
				if "Queue" in status and "PC" in status:
					two_pc_in_queue.append(sam_name)
				elif "In Progress" in status and "PC" in status:
					two_pc_inprogress.append(sam_name)
				elif "On Hold" in status and "PC" in status:
					two_pc_on_hold.append(sam_name)
				elif "Rejected" in status and "PC" in status:
					two_pc_rejected.append(sam_name)
				elif "Completed" in status and "PC" in status:
					two_pc_completed.append(sam_name)
				elif "Queue" in status and "GML" in status:
					two_gml_in_queue.append(sam_name)
				elif "In Progress" in status and "GML" in status:
					two_gml_inprogress.append(sam_name)
				elif "On Hold" in status and "GML" in status:
					two_gml_on_hold.append(sam_name)
				elif "Rejected" in status and "GML" in status:
					two_gml_rejected.append(sam_name)
				elif "Completed" in status and "GML" in status:
					two_gml_completed.append(sam_name)

		
			

	one_pc_count=[len(one_pc_in_queue),len(one_pc_inprogress),len(one_pc_completed),len(one_pc_on_hold),len(one_pc_rejected)]
	two_pc_count=[len(two_pc_in_queue),len(two_pc_inprogress),len(two_pc_completed),len(two_pc_on_hold),len(two_pc_rejected)]
	one_gml_count=[len(one_gml_in_queue),len(one_gml_inprogress),len(one_gml_completed),len(one_gml_on_hold),len(one_gml_rejected)]
	two_gml_count=[len(two_gml_in_queue),len(two_gml_inprogress),len(two_gml_completed),len(two_gml_on_hold),len(two_gml_rejected)]

	return [one_pc_count,two_pc_count],[one_gml_count,two_gml_count]


#LDM Report
ldm_input_date=[]

#1st month
one_ldm_in_queue=[]
one_ldm_inprogress=[]
one_ldm_on_hold=[]
one_ldm_completed=[]
one_ldm_rejected=[]

#2nd month
two_ldm_in_queue=[]
two_ldm_inprogress=[]
two_ldm_on_hold=[]
two_ldm_completed=[]
two_ldm_rejected=[]

#3rd month
third_ldm_in_queue=[]
third_ldm_inprogress=[]
third_ldm_on_hold=[]
third_ldm_completed=[]
third_ldm_rejected=[]

# ldm_inprogress_status=["In Progress - LocID Matching","In Progress - LocID Matching Completed","In Progress - Repurposing","In Progress - Repurposing Completed","In Progress - Address Alignment","In Progress - Address Alignment Completed","In Progress - Final Validations",]
# ldm_queue_status=["In Queue - To be Assigned",]
# ldm_completed_status=["Completed - Handover done",]
# ldm_on_hold_status=["On Hold",]
# ldm_rejected_status=["Rejected",]

def ldm_report():
	for i in range(ldm.nrows):
		input_date=ldm.cell(i,8).value
		status=ldm.cell(i,6).value
		sam_name=ldm.cell(i,0).value
		if type(input_date) == float:
			date=xlrd.xldate_as_tuple(ldm.cell(i,8).value,master_tracker.datemode)
			today=datetime.now().month
			if today==date[1]:
				if "In Queue" in status:
					one_ldm_in_queue.append(sam_name)
				elif "In Progress" in status:
					one_ldm_inprogress.append(sam_name)
				elif "On Hold" in status:
					one_ldm_on_hold.append(sam_name)
				elif "Rejected" in status:
					one_ldm_rejected.append(sam_name)
				elif "Handover done" in status:
					one_ldm_completed.append(sam_name)


			if today==1:
				if date[1]==12:
					if "In Queue" in status:
						two_ldm_in_queue.append(sam_name)
					elif "In Progress" in status:
						two_ldm_inprogress.append(sam_name)
					elif "On Hold" in status:
						two_ldm_on_hold.append(sam_name)
					elif "Rejected" in status:
						two_ldm_rejected.append(sam_name)
					elif "Handover done" in status:
						two_ldm_completed.append(sam_name)

				if date[1]==11:
					if "In Queue" in status:
						third_ldm_in_queue.append(sam_name)
					elif "In Progress" in status:
						third_ldm_inprogress.append(sam_name)
					elif "On Hold" in status:
						third_ldm_on_hold.append(sam_name)
					elif "Rejected" in status:
						third_ldm_rejected.append(sam_name)
					elif "Handover done" in status:
						third_ldm_completed.append(sam_name)

			elif today==2:
				if date[1]==1:
					if "In Queue" in status:
						two_ldm_in_queue.append(sam_name)
					elif "In Progress" in status:
						two_ldm_inprogress.append(sam_name)
					elif "On Hold" in status:
						two_ldm_on_hold.append(sam_name)
					elif "Rejected" in status:
						two_ldm_rejected.append(sam_name)
					elif "Handover done" in status:
						two_ldm_completed.append(sam_name)

				if date[1]==12:
					if "In Queue" in status:
						third_ldm_in_queue.append(sam_name)
					elif "In Progress" in status:
						third_ldm_inprogress.append(sam_name)
					elif "On Hold" in status:
						third_ldm_on_hold.append(sam_name)
					elif "Rejected" in status:
						third_ldm_rejected.append(sam_name)
					elif "Handover done" in status:
						third_ldm_completed.append(sam_name)

			else:
				if date[1]==(date[1]-1):
					if "In Queue" in status:
						two_ldm_in_queue.append(sam_name)
					elif "In Progress" in status:
						two_ldm_inprogress.append(sam_name)
					elif "On Hold" in status:
						two_ldm_on_hold.append(sam_name)
					elif "Rejected" in status:
						two_ldm_rejected.append(sam_name)
					elif "Handover done" in status:
						two_ldm_completed.append(sam_name)
				if date[1]==(date[1]-2):
					if "In Queue" in status:
						third_ldm_in_queue.append(sam_name)
					elif "In Progress" in status:
						third_ldm_inprogress.append(sam_name)
					elif "On Hold" in status:
						third_ldm_on_hold.append(sam_name)
					elif "Rejected" in status:
						third_ldm_rejected.append(sam_name)
					elif "Handover done" in status:
						third_ldm_completed.append(sam_name)

	one_ldm_count=[len(one_ldm_in_queue),len(one_ldm_inprogress),len(one_ldm_completed),len(one_ldm_on_hold),len(one_ldm_rejected)]
	two_ldm_count=[len(two_ldm_in_queue),len(two_ldm_inprogress),len(two_ldm_completed),len(two_ldm_on_hold),len(two_ldm_rejected)]
	third_ldm_count=[len(third_ldm_in_queue),len(third_ldm_inprogress),len(third_ldm_completed),len(third_ldm_on_hold),len(third_ldm_rejected)]
	return [one_ldm_count,two_ldm_count,third_ldm_count]

#DSG IAB Report


#1st month
one_dsg_iab_in_queue=[]
one_dsg_iab_inprogress=[]
one_dsg_iab_on_hold=[]
one_dsg_iab_completed=[]
one_dsg_iab_rejected=[]

#2nd month
two_dsg_iab_in_queue=[]
two_dsg_iab_inprogress=[]
two_dsg_iab_on_hold=[]
two_dsg_iab_completed=[]
two_dsg_iab_rejected=[]

#3rd month
third_dsg_iab_in_queue=[]
third_dsg_iab_inprogress=[]
third_dsg_iab_on_hold=[]
third_dsg_iab_completed=[]
third_dsg_iab_rejected=[]
dsg_iab_inprogress_status=["In Progress","In Progress - HFC Completed",]
dsg_iab_queue_status=["In Queue - To be Assigned","In Queue - HFC Completed",]
dsg_iab_completed_status=["Completed",]
dsg_iab_on_hold_status=["On Hold - HFC Completed","On Hold - PNI Issues","On Hold - Data Issues","On Hold - Document Unavailability","On Hold - Awaiting Upstream team Updates","On Hold - PNI Issues","On Hold - Data Issues","On Hold - Document Unavailability","On Hold - Awaiting Upstream team Updates",]
dsg_iab_rejected_status=["Rejected",]
def dsg_iab_report():
	for i in range(dsg_iab.nrows):
		input_date=dsg_iab.cell(i,8).value
		status=dsg_iab.cell(i,6).value
		sam_name=dsg_iab.cell(i,0).value
		if type(input_date) == float:
			date=xlrd.xldate_as_tuple(dsg_iab.cell(i,8).value,master_tracker.datemode)
			today=datetime.now().month
			if today==date[1]:
				if "In Queue" in status:
					one_dsg_iab_in_queue.append(sam_name)
				elif "In Progress" in status:
					one_dsg_iab_inprogress.append(sam_name)
				elif "On Hold" in status:
					one_dsg_iab_on_hold.append(sam_name)
				elif "Rejected" in status:
					one_dsg_iab_rejected.append(sam_name)
				elif "Completed" in status:
					one_dsg_iab_completed.append(sam_name)
			if today==1:
				if date[1]==12:
					if "In Queue" in status:
						two_dsg_iab_in_queue.append(sam_name)
					elif "In Progress" in status:
						two_dsg_iab_inprogress.append(sam_name)
					elif "On Hold" in status:
						two_dsg_iab_on_hold.append(sam_name)
					elif "Rejected" in status:
						two_dsg_iab_rejected.append(sam_name)
					elif "Completed" in status:
						two_dsg_iab_completed.append(sam_name)

				if date[1]==11:
					if "In Queue" in status:
						third_dsg_iab_in_queue.append(sam_name)
					elif "In Progress" in status:
						third_dsg_iab_inprogress.append(sam_name)
					elif "On Hold" in status:
						third_dsg_iab_on_hold.append(sam_name)
					elif "Rejected" in status:
						third_dsg_iab_rejected.append(sam_name)
					elif "Completed" in status:
						third_dsg_iab_completed.append(sam_name)


			elif today==2:
				if date[1]==1:
					if "In Queue" in status:
						two_dsg_iab_in_queue.append(sam_name)
					elif "In Progress" in status:
						two_dsg_iab_inprogress.append(sam_name)
					elif "On Hold" in status:
						two_dsg_iab_on_hold.append(sam_name)
					elif "Rejected" in status:
						two_dsg_iab_rejected.append(sam_name)
					elif "Completed" in status:
						two_dsg_iab_completed.append(sam_name)

				if date[1]==12:
					if "In Queue" in status:
						third_dsg_iab_in_queue.append(sam_name)
					elif "In Progress" in status:
						third_dsg_iab_inprogress.append(sam_name)
					elif "On Hold" in status:
						third_dsg_iab_on_hold.append(sam_name)
					elif "Rejected" in status:
						third_dsg_iab_rejected.append(sam_name)
					elif "Completed" in status:
						third_dsg_iab_completed.append(sam_name)

			else:
				if date[1]==(date[1]-1):
					if "In Queue" in status:
						two_dsg_iab_in_queue.append(sam_name)
					elif "In Progress" in status:
						two_dsg_iab_inprogress.append(sam_name)
					elif "On Hold" in status:
						two_dsg_iab_on_hold.append(sam_name)
					elif "Rejected" in status:
						two_dsg_iab_rejected.append(sam_name)
					elif "Completed" in status:
						two_dsg_iab_completed.append(sam_name)

				if date[1]==(date[1]-2):
					if "In Queue" in status:
						third_dsg_iab_in_queue.append(sam_name)
					elif "In Progress" in status:
						third_dsg_iab_inprogress.append(sam_name)
					elif "On Hold" in status:
						third_dsg_iab_on_hold.append(sam_name)
					elif "Rejected" in status:
						third_dsg_iab_rejected.append(sam_name)
					elif "Completed" in status:
						third_dsg_iab_completed.append(sam_name)

	return []
