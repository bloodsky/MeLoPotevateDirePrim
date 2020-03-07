import LinkedList

class DoubleRecord(LinkedList.Record):
    def __init__(self,elem):
        LinkedList.Record.__init__(self,elem)
        self.prev=None

class ListaDoppiamenteCollegata(LinkedList.ListaCollegata):
    
    def addAsLast(self,elem):
        rec= DoubleRecord(elem)
        if self.first==None:
            self.first=self.last=rec
        else:
            rec.prev = self.last
            self.last.next = rec
            self.last = rec
    
    def addAsFirst(self,elem):
        rec=DoubleRecord(elem)
        if self.first==None:
            self.first=self.last=rec
        else:
            self.first.prev = rec
            rec.next = self.first
            self.first = rec
    
    def popFirst(self):
        if self.first==None:
            return None
        else:
            res = self.first.elem
            self.first = self.first.next
            if self.first!=None:
                self.first.prev = None #Il controllo serve a gestire il caso di lista vuota    
            else:
                self.last = None
            return res
    
    #Ora possiamo cancellare efficientemente anche l'ultimo.
    def popLast(self):
        if self.first==None:
            return None
        else:
            res = self.last.elem
            self.last = self.last.prev
            if self.last!=None:
                self.last.next = None
            else:
                self.first = None
            return res
    #Ora possiamo cancellare efficientemente anche un record generico.
    def deleteRecord(self,rec):
        if rec==None:
            return  #restituisce None!
        if rec.prev!=None:
            rec.prev.next = rec.next
        else:
            self.first = rec.next
        if rec.next!=None:
            rec.next.prev = rec.prev
        else:
            self.last = rec.prev