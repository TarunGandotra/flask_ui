import os
import sys
from bs4 import BeautifulSoup

def CHE015_11(xmlpath):
    
    try:
        
        final = []
        
        xml = open(xmlpath,"r",encoding="utf-8")
        soup = BeautifulSoup(xml,'lxml')
        soup1=str(soup)
        
        glyph = soup.find_all('ce:glyph')
        
        for i in glyph:
            
            if i['name'] == 'tbnd':
                
                if i.next[0] in ['C','N','P','S']:
                    continue
                    
                elif i.next[0] == 'H':
                    continue
                
                elif i.next[0] == ' ':
                    continue
                    
                else:
                    
                    f=["CHE015","Chemistry","The triple bond glyph (<ce:glyph name=tbond/>) should be used to indicate a triple bond","Error",str(soup1.index(i.next)),"Triple bond not suitable!"]
                    final.append(f)
            
            elif i['name'] == 'dbnd':
                
                if i.next[0] in ['C','N','P','S','O']:
                    continue
                
                elif i.next[0] == 'H':
                    continue
                    
                elif i.next[0] == ' ':
                    continue
                    
                else:
                    
                    f=["CHE015","Chemistry","The triple bond glyph (<ce:glyph name=tbond/>) should be used to indicate a triple bond","Error",str(soup1.index(i.next)),"Double bond not suitable!"]
                    final.append(f)
            
            elif i['name'] == 'sbnd':
                
                if i.next[0] in ['C','H','N','P','S','O','F']:
                    continue
                
                elif i.next[0] == ' ':
                    continue
                    
                else:
                    
                    f=["CHE015","Chemistry","The triple bond glyph (<ce:glyph name=tbond/>) should be used to indicate a triple bond","Error",str(soup1.index(i.next)),"Single bond not suitable!"]
                    final.append(f)

        if final==[]:
            
            f=["CHE015","Chemistry","aid","no error"]
            final.append(f)
        
        return final
    
    except Exception as e:
        
        #print(e.with_traceback())
        final=[]
        f=["CHE015","Chemistry","The triple bond glyph (<ce:glyph name=tbond/>) should be used to indicate a triple bond","no error"]
        final.append(f)
        logging.info('='*50)
        logging.exception("Got exception on main handler in CHE015 Chemistry ")
        logging.shutdown()
        
        return final
