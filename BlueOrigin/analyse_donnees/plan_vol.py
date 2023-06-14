import math
import numpy as np

class PlanVol():

    def __init__(self,
                 data : list):
        self.data = data

    def creer_plan_vol(self):
        
        tp_ignition=0
        tp_liftoff=0	
        tp_MECO=0		
        tp_apogee=0			
        tp_deploy_brakes=0		
        tp_restart_ignition=0
        tp_touchdown=0
        
        altitude_liftoff=self.data[1][9]
        i=2
        while tp_liftoff==0 or tp_MECO==0 or tp_apogee==0 or tp_deploy_brakes==0 or tp_restart_ignition==0 or tp_touchdown==0:
            altitude=self.data[i][9]
            altitude_before=self.data[i][9]
            deltaV=np.linalg.norm([self.data[i][4],self.data[i][5],self.data[i][6]])-np.linalg.norm([self.data[i-1][4],self.data[i-1][5],self.data[i-1][6]])
            deltaV_before=np.linalg.norm([self.data[i-1][4],self.data[i-1][5],self.data[i-1][6]])-np.linalg.norm([self.data[i-2][4],self.data[i-2][5],self.data[i-2][6]])

            if tp_liftoff==0 and altitude-altitude_liftoff>=1: 
                tp_liftoff=self.data[i][0]
                
            elif tp_liftoff!=0 and tp_MECO==0 and -9.81<deltaV<-9.5:
                tp_MECO=self.data[i][0]
                
            elif tp_MECO!=0 and tp_apogee==0 and np.sign(altitude-altitude_before)==-1:
                tp_apogee=self.data[i][0]
                
            elif  tp_apogee!=0 and tp_deploy_brakes==0 and np.sign(deltaV-deltaV_before)==-1 and -10<deltaV<0:
                tp_deploy_brakes=self.data[i][0]
                
            elif tp_deploy_brakes!=0 and tp_restart_ignition==0 and np.sign(deltaV-deltaV_before)==-1 and -10<deltaV<0:
                tp_deploy_brakes=self.data[i][0]
                
            elif tp_restart_ignition!=0 and tp_touchdown==0 and altitude-altitude_liftoff<=1:
                tp_touchdown=self.data[i][0]
            
            i+=1
        
            
        
        
        
        
        
        
        
        plan_vol_final = {'ignition':tp_ignition,'liftof':tp_liftoff,'MECO':tp_MECO,'apogee':tp_apogee,'deploy_brake':tp_deploy_brakes,'restart ignition':tp_restart_ignition,'touch down':tp_touchdown}
        

        return plan_vol_final