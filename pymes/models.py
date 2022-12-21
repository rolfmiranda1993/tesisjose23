from django.db import models
from automatic_crud.models import BaseModel
from members.models import departamentoD,rubroD,clienteD
#from members.models import StaffProfile
# Create your models here.
class cliente(BaseModel):
    pagos =((u'1',u'Efectivo'),
    (u'2',u'Cheque'),
    (u'3',u'Transferencia'),
    (u'4',u'Deposito'),
    )

    cuentas =((u'Corriente',u'Corriente'),
    (u'Ahorro',u'Ahorro'),
    (u'Chequera',u'Chequera'),
    (u'Nomina',u'Nomina'),
    (u'Dolares',u'Dolares'),
    )

    nombre_de_la_empresa = models.CharField('Empresa',max_length=250)
    numero_de_ruc = models.CharField('RUC', max_length=250)
    nombre_del_nexo = models.CharField('Nexo', max_length=250, null=True, blank=True)
    telefono_del_nexo = models.CharField('Tel. Nexo', max_length=250, null=True, blank=True)
    mail_del_nexo = models.CharField('Mail Nexo', max_length=250, null=True, blank=True)
    nombre_contacto_pagos = models.CharField('Contacto de pago', max_length=250, null=True, blank=True)
    telefono_contacto_pagos = models.CharField('Tel. Conacto Pago', max_length=250, null=True, blank=True)
    mail_contacto_pagos = models.CharField('Mail Conacto Pago', max_length=250, null=True, blank=True)
    fecha_de_vinculacion = models.DateField('Fecha de Vinculacion')
    notas_adicionales = models.CharField('Notas', max_length=250, null=True, blank=True)
    forma_de_pago_habitual = models.CharField('Pago Habitual', max_length=20, choices=pagos, null=True, blank=True)
    banco = models.CharField('Banco', max_length=250, null=True, blank=True)
    titular_de_la_cuenta = models.CharField('Titular de la cuenta', max_length=250, null=True, blank=True)
    tipo_de_cuenta = models.CharField('Tipo de Cuenta', max_length=250, choices=cuentas, null=True, blank=True)
    numero_de_cuenta = models.CharField('Nro de Cuenta', max_length=250, null=True, blank=True)
    documento_de_cuenta = models.CharField('Documento', max_length=250, null=True, blank=True)

    all_cruds_types = False
    normal_cruds = True
    ajax_crud = False

    class meta:
        Verbose_name = 'cliente'
        Verbose_name_plural = 'clientes'
    
    def ___str__(self):
        #return self.nombre_de_la_empresa
        return str(self.nombre_de_la_empresa) + ' - ' + self.numero_de_ruc

class departamento(BaseModel):
    nivel_jerarquia=(
        (u'1',u'1'),
        (u'2',u'2'),
        (u'3',u'3'),
        (u'4',u'4'),
        (u'5',u'5'),
        (u'6',u'6'),
        )
    nombre = models.CharField('Nombre de departamento', max_length=200)
    jerarquia = models.CharField('Jerarquia asignada',max_length=20, choices=nivel_jerarquia)
    
    all_cruds_types = False
    normal_cruds = True
    ajax_crud = False

    normal_pagination=True
    
    def ___str__(self):
        return str(self.nombre)

class rubro(BaseModel):
    area = models.ForeignKey(departamentoD, on_delete=models.CASCADE)
    nombre = models.CharField('Nombre', max_length=200)
    
    all_cruds_types = False
    normal_cruds = True
    ajax_crud = False

    normal_pagination=True
    
    def ___str__(self):
        return str(self.nombre)

class ingreso(BaseModel):
    pagos =((u'1',u'Efectivo'),
    (u'2',u'Cheque'),
    (u'3',u'Transferencia'),
    (u'4',u'Deposito'),
    )
    nombre = models.CharField('Nombre', max_length=250)
    rubro = models.ForeignKey(rubroD, on_delete=models.CASCADE)
    forma_de_pago = models.CharField('Forma de Pago', max_length=200, choices=pagos, null=True, blank=True)
    tipo_de_cobro = models.CharField('Tipo de cobro', max_length=200, choices=pagos, null=True, blank=True)
    nombre_de_pago = models.CharField('Nombre de Pago',max_length=200)
    titular_de_pago = models.ForeignKey(clienteD, on_delete=models.CASCADE)
    monto_de_pago = models.IntegerField('Monto de Pago')
    numero_de_factura = models.CharField('Factura Nro', max_length=200)

    all_cruds_types = False
    normal_cruds = True
    ajax_crud = False

    normal_pagination=True
    
    class Meta:
        verbose_name = 'ingreso'
        verbose_name_plural = 'ingresos'

    def __str__(self):
        return str(self.nombre)

class egreso(BaseModel):
    nombre = models.CharField('Nombre', max_length=250)
    rubro = models.ForeignKey(rubroD, on_delete=models.CASCADE)
    forma_de_pago = models.CharField('Forma de Pago', max_length=200)
    tipo_de_pago = models.CharField('Tipo de Pago', max_length=200)
    nombre_de_pago = models.CharField('Nombre de Pago', max_length=200)
    titular_de_pago = models.ForeignKey(clienteD, on_delete=models.CASCADE)
    monto_de_pago = models.IntegerField('Monto de Pago')
    numero_de_factura = models.CharField('Factura Nro', max_length=200)

    all_cruds_types = False
    normal_cruds = True
    ajax_crud = False
    
    normal_pagination=True

    class meta:
        Verbose_name = 'egreso'
        Verbose_name_plural = 'egresos'
    
    def ___str__(self):
        return str(self.nombre)
"""
class departamento(BaseModel):
    nivel_jerarquia=(
        (u'1',u'1'),
        (u'2',u'2'),
        (u'3',u'3'),
        (u'4',u'4'),
        (u'5',u'5'),
        (u'6',u'6'),
        )
    nombre = models.CharField('Nombre de departamento', max_length=200)
    jerarquia = models.CharField('Jerarquia asignada',max_length=20, choices=nivel_jerarquia)
    
    all_cruds_types = False
    normal_cruds = True
    ajax_crud = False

    normal_pagination=True

    class meta:
        Verbose_name = 'departamento'
        Verbose_name_plural = 'departamentos'
    
    def ___str__(self):
        cadena = self.id + '-' +self.nombre
        return cadena #str(self.id) + '-' + (self.nombre)

class miembro(BaseModel):
    EST = ((u'Soltero',u'Soltero'),
    (u'Casado',u'Casado'),
    (u'Viudo',u'Viudo'),
    (u'Divorciado',u'Divorciado'),
    )
    HIJ = ((u'Si',u'Si'),
    (u'No',u'No'),
    )
    GEN = ((u'H',u'Hombre'),
    (u'M',u'Mujer'),
    (u'PNM',u'Prefiero no mencionarlo'),
    )

    all_cruds_types = False
    normal_cruds = True
    ajax_crud = False

    normal_pagination=True

    nombres = models.CharField('Nombres', max_length=250)
    apellidos = models.CharField('Apellidos', max_length=250)
    nacionalidad = models.CharField('Nacionalidad', max_length=250)
    numero_de_documento = models.CharField('CIN', max_length=250)
    fecha_de_nacimiento = models.DateField('Fecha de Nacimiento')
    telefono_particular = models.CharField('Tel. Part.', max_length=250)
    telefono_corporativo = models.CharField('Tel. Corp.', max_length=250)
    mail_particular = models.CharField('Mail Part.', max_length=250)
    mail_corporativo = models.CharField('Mail Corp.', max_length=250)
    fecha_de_ingreso = models.DateField('Fecha de Ingreso')
    fecha_de_salida = models.DateField('Fecha de Salida')
    motivo_de_salida = models.CharField('Motivo de Salida', max_length=250)
    cargo = models.CharField('Cargo', max_length=250)
    notas_adicionales = models.CharField('Notas', max_length=250)
    contribuyente_set = models.CharField('SET', max_length=20, choices=HIJ)
    estado_civil= models.CharField('Estado Civil', max_length=25, choices=EST)
    hijos = models.CharField('Hijos', max_length=25, choices=HIJ)
    genero = models.CharField('Genero', max_length=25, choices=GEN)
    
    class meta:
        Verbose_name = 'miembro'
        Verbose_name_plural = 'miembros'

    def __str__(self):
       return str(self.nombres) + ' - ' + self.apellidos

class rubro(BaseModel):
    area = models.ForeignKey(departamento, on_delete=models.CASCADE)
    nombre = models.CharField('Nombre', max_length=200)
    
    all_cruds_types = False
    normal_cruds = True
    ajax_crud = False

    normal_pagination=True

    class meta:
        Verbose_name = 'rubro'
        Verbose_name_plural = 'rubros'
    
    def ___str__(self):
        return str(self.nombre) + ' - '

class ingreso(BaseModel):
    nombre = models.CharField('Nombre', max_length=250)
    rubro = models.ForeignKey(rubro, on_delete=models.CASCADE)
    forma_de_pago = models.CharField('Forma de Pago', max_length=200)
    tipo_de_cobro = models.CharField('Tipo de cobro', max_length=200)
    nombre_de_pago = models.CharField('Nombre de Pago',max_length=200)
    titular_de_pago = models.ForeignKey(cliente, on_delete=models.CASCADE)
    monto_de_pago = models.IntegerField('Monto de Pago')
    numero_de_factura = models.CharField('Factura Nro', max_length=200)

    all_cruds_types = False
    normal_cruds = True
    ajax_crud = False

    normal_pagination=True
    
    class Meta:
        verbose_name = 'ingreso'
        verbose_name_plural = 'ingresos'

    def __str__(self):
        return str(self.nombre)

class egreso(BaseModel):
    nombre = models.CharField('Nombre', max_length=250)
    rubro = models.ForeignKey(rubro, on_delete=models.CASCADE)
    forma_de_pago = models.CharField('Forma de Pago', max_length=200)
    tipo_de_pago = models.CharField('Tipo de Pago', max_length=200)
    nombre_de_pago = models.CharField('Nombre de Pago', max_length=200)
    titular_de_pago = models.ForeignKey(cliente, on_delete=models.CASCADE)
    monto_de_pago = models.IntegerField('Monto de Pago')
    numero_de_factura = models.CharField('Factura Nro', max_length=200)

    all_cruds_types = False
    normal_cruds = True
    ajax_crud = False
    
    normal_pagination=True

    class meta:
        Verbose_name = 'egreso'
        Verbose_name_plural = 'egresos'
    
    def ___str__(self):
        return str(self.nombre)


class rol(BaseModel):
    nombre = models.CharField('Nombre', max_length=250)
    empleado_o_proveedor = models.ForeignKey(cliente, on_delete=models.CASCADE)
    nombre_de_area = models.ForeignKey(departamento, on_delete=models.CASCADE)
    
    all_cruds_types = False
    normal_cruds = True
    ajax_crud = False

    normal_pagination=True

    class meta:
        Verbose_name = 'rol'
        Verbose_name_plural = 'roles'
    
    def ___str__(self):
        return str(self.nombre)

class tarea(BaseModel):
    nombre = models.CharField('Nombre', max_length=200)
    descripcion = models.CharField('Descripcion',max_length=200)
    fecha_entrega = models.DateField('Fecha de entrega')
    hora_entrega = models.TimeField('Hora de Entrega')
    responsable = models.ForeignKey(miembro, on_delete=models.CASCADE)

    all_cruds_types = False
    normal_cruds = True
    ajax_crud = False

    normal_pagination=True
        
    class meta:
        Verbose_name = 'tarea'
        Verbose_name_plural = 'tareas'
   
    def ___str__(self):
        return str(self.nombre)

class carga(BaseModel):
    nombre = models.CharField('Nombre de carga', max_length=200)
    motivo = models.CharField('Motivo',max_length=20)
    staff = models.ForeignKey(StaffProfile, on_delete=models.CASCADE)

    all_cruds_types = False
    normal_cruds = True
    ajax_crud = False

    normal_pagination=True

    class meta:
        Verbose_name = 'carga'
        Verbose_name_plural = 'cargas'
    
    def ___str__(self):
        return str(self.nombre)

class carga_par(BaseModel):
    nombre = models.CharField('Nombre de carga', max_length=200)
    motivo = models.CharField('Motivo',max_length=20)
    staff = models.ForeignKey(StaffProfile, on_delete=models.CASCADE)
    dpto = models.ForeignKey(departamento, on_delete=models.CASCADE)
    
    all_cruds_types = False
    normal_cruds = True
    ajax_crud = False

    normal_pagination=True

    class meta:
        Verbose_name = 'carga_par'
        Verbose_name_plural = 'carga_pares'
    
    def ___str__(self):
        return str(self.nombre)
"""