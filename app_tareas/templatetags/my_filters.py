from django import template

register = template.Library()

@register.filter

def obtener_color_etiqueta(etiqueta_nombre):
    colores={
        "Hogar": "#e5b6f2",
        "Trabajo": "#B6C5F2",
        "Estudio": "#B6F2D0",
        "Personal": "#F2E3B6"
    }
    
    return colores.get(etiqueta_nombre, "#777777")
