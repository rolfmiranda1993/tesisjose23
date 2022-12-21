from django.db import models
from automatic_crud.models import BaseModel


# Create your models here.

class clienteD(BaseModel):  # Staff information
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

    staff_name = models.CharField('Empresa',max_length=200)
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

    normal_pagination=True
    def __str__(self):
        return str(self.staff_name)

class departamentoD(BaseModel):  # Staff information
    nivel_jerarquia=(
        (u'1',u'1'),
        (u'2',u'2'),
        (u'3',u'3'),
        )
    #name = models.CharField('Nombre de departamento', max_length=200)
    #staff_no = models.IntegerField('Numero' primary_key=True)
    staff_name = models.TextField('Nombre de departamento', max_length=200)
    jerarquia = models.CharField('Jerarquia asignada',max_length=20, choices=nivel_jerarquia)
    
    all_cruds_types = False
    normal_cruds = True
    ajax_crud = False

    normal_pagination=True
    def __str__(self):
        return str(self.staff_name)

class rubroD(BaseModel):  # Staff information
    area = models.ForeignKey(departamentoD, on_delete=models.CASCADE)
    staff_name = models.CharField('Nombre', max_length=200)
    
    all_cruds_types = False
    normal_cruds = True
    ajax_crud = False

    normal_pagination=True
    def __str__(self):
        return str(self.staff_name)

class StaffProfile(models.Model):  # Staff information
    staff_no = models.IntegerField(primary_key=True)
    staff_name = models.TextField(max_length=200)
    designation = models.CharField(max_length=100)
    reporting_officer = models.IntegerField()

    def __str__(self):
        return str(self.staff_no) + '-' + self.staff_name