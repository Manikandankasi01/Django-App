import os
import xlrd
from datetime import datetime
import datetime as d
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
tracker_path=os.path.join(base_path,'templates','MasterTracker')

#m_tracker=pd.ExcelFile(tracker_path+"\\Master_Tracker_v8.6.xlsx")
# desg=pd.read_excel(tracker_path+"\\Master_Tracker_v8.6.xlsx",sheetname="DESG T18 Allocation")
#
master_tracker=xlrd.open_workbook(tracker_path+"\\Master_Tracker_v8.6.xlsx")
#master_tracker=xlrd.open_workbook(tracker_path+"\\Master_Tracker_v8.6.xlsx")

desg_pdc=master_tracker.sheet_by_name("DESG PDC Allocation")
desg=master_tracker.sheet_by_name("DESG T18 Allocation")
ldm=master_tracker.sheet_by_name("LDM Allocation")
dsg_iab=master_tracker.sheet_by_name("DSG - IAB Allocation")
ndq_iab=master_tracker.sheet_by_name("NDQ - IAB Allocation")
dsg_fab=master_tracker.sheet_by_name("DSG - FAB Allocation")
ndq_fab=master_tracker.sheet_by_name("NDQ - FAB Allocation")
transit=master_tracker.sheet_by_name("Transit Allocation")

today=datetime.now()


def pdc_report(s_date,e_date):
	pdc_in_queue=[]
	pdc_inprogress=[]
	pdc_on_hold=[]
	pdc_completed=[]
	pdc_rejected=[]
	delta_in_queue=[]
	delta_inprogress=[]
	delta_on_hold=[]
	delta_completed=[]
	delta_rejected=[]
	today

	for i in range(desg_pdc.nrows):
		input_date=desg_pdc.cell(i,8).value
		status=desg_pdc.cell(i,6).value
		sam_name=desg_pdc.cell(i,0).value
		category=desg_pdc.cell(i,4).value
		if type(input_date) == float:
			date=xlrd.xldate_as_tuple(desg_pdc.cell(i,8).value,master_tracker.datemode)
			date=datetime(*date[0:6])
			if s_date<=date and e_date>=date:
				if category=="PDC":
					if "In Queue" in status:
						pdc_in_queue.append(sam_name)
					elif "In Progress" in status:
						pdc_inprogress.append(sam_name)
					elif "On Hold" in status:
						pdc_on_hold.append(sam_name)
					elif "Rejected" in status:
						pdc_rejected.append(sam_name)
					elif ("PDC completed" in status) or ("AFR Load Completed" in status) or ("Completed" in status):
						pdc_completed.append(sam_name)
				else:
					if "In Queue" in status:
						delta_in_queue.append(sam_name)
					elif "In Progress" in status:
						delta_inprogress.append(sam_name)
					elif "On Hold" in status:
						delta_on_hold.append(sam_name)
					elif "Rejected" in status:
						delta_rejected.append(sam_name)
					elif ("Delta completed" in status) or ("AFR Load Completed" in status) or ("Completed" in status):
						delta_completed.append(sam_name)

	delta=[len(delta_in_queue),len(delta_inprogress),len(delta_completed), len(delta_on_hold),len(delta_rejected)]
	pdc=[len(pdc_in_queue),len(pdc_inprogress),len(pdc_completed), len(pdc_on_hold),len(pdc_rejected)]
	return pdc,delta

def desg_report(s_date,e_date):
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

	for i in range(desg.nrows):
		input_date=desg.cell(i,7).value
		st=desg.cell(i,6).value
		status=st.strip()
		sam_name=desg.cell(i,0).value
		if type(input_date) == float:
			date=xlrd.xldate_as_tuple(desg.cell(i,7).value,master_tracker.datemode)
			date=datetime(*date[0:6])
			#diff=today-date
			#print (s_date,">= im outside ",date,"and ",e_date,"<=",date)
			if s_date<=date and e_date>=date:
				#print (s_date,">=i in inside if loop",date,"and ",e_date,"<=",date)
				if "Queue" in status and "PC" in status:
					one_pc_in_queue.append(sam_name)
				elif "In Progress" in status and "PC" in status:
					one_pc_inprogress.append(sam_name)
				elif "Hold" in status and "PC" in status:
					one_pc_on_hold.append(sam_name)
				elif "Rejected" in status and "PC" in status:
					one_pc_rejected.append(sam_name)
				elif "Completed" in status and "PC" in status:
					one_pc_completed.append(sam_name)
				elif "Queue" in status and "GML" in status:
					one_gml_in_queue.append(sam_name)
				elif "In Progress" in status and "GML" in status:
					one_gml_inprogress.append(sam_name)
				elif "Hold" in status and "GML" in status:
					one_gml_on_hold.append(sam_name)
				elif "Rejected" in status and "GML" in status:
					one_gml_rejected.append(sam_name)
				elif "Completed" in status and "GML" in status:
					one_gml_completed.append(sam_name)

	one_pc_count=[len(one_pc_in_queue),len(one_pc_inprogress),len(one_pc_completed),len(one_pc_on_hold),len(one_pc_rejected)]
	one_gml_count=[len(one_gml_in_queue),len(one_gml_inprogress),len(one_gml_completed),len(one_gml_on_hold),len(one_gml_rejected)]
	return one_pc_count,one_gml_count


def ldm_report(s_date,e_date):
	one_ldm_in_queue=[]
	one_ldm_inprogress=[]
	one_ldm_on_hold=[]
	one_ldm_completed=[]
	one_ldm_rejected=[]

	for i in range(ldm.nrows):
		input_date=ldm.cell(i,8).value
		status=ldm.cell(i,6).value
		sam_name=ldm.cell(i,0).value
		if type(input_date) == float:
			date=xlrd.xldate_as_tuple(ldm.cell(i,8).value,master_tracker.datemode)
			date=datetime(*date[0:6])
			diff=today-date
			if s_date<=date and e_date>=date:
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

	one_ldm_count=[len(one_ldm_in_queue),len(one_ldm_inprogress),len(one_ldm_completed),len(one_ldm_on_hold),len(one_ldm_rejected)]
	return one_ldm_count


def dsg_iab_report(s_date,e_date):
	one_dsg_iab_in_queue=[]
	one_dsg_iab_inprogress=[]
	one_dsg_iab_on_hold=[]
	one_dsg_iab_completed=[]
	one_dsg_iab_rejected=[]

	for i in range(dsg_iab.nrows):
		input_date=dsg_iab.cell(i,10).value
		status=dsg_iab.cell(i,9).value
		sam_name=dsg_iab.cell(i,0).value
		if type(input_date) == float:
			date=xlrd.xldate_as_tuple(dsg_iab.cell(i,10).value,master_tracker.datemode)
			date=datetime(*date[0:6])
			diff=today-date
			if s_date<=date and e_date>=date:
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

	weekly=[len(one_dsg_iab_in_queue),len(one_dsg_iab_inprogress),len(one_dsg_iab_completed), len(one_dsg_iab_on_hold),len(one_dsg_iab_rejected)]
	return weekly


if __name__ == "__main__":
	print ("im here")
	
