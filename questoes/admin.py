from django.contrib import admin
from .models import Disciplina, Assunto, Questao

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'origem')
    search_fields = ('nome',)
    ordering = ('nome',)

@admin.register(Assunto)
class AssuntoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'disciplina_nome')
    search_fields = ('nome',)
    ordering = ('nome',)
    list_filter = ['disciplina']

    def disciplina_nome(self, obj):
        return obj.disciplina.nome
    disciplina_nome.short_description = 'Disciplina'

@admin.register(Questao)
class QuestaoAdmin(admin.ModelAdmin):
    list_display = ('disciplina_nome', 'assunto_nome', 'latex_text', 'gabarito', 'dificuldade', 'imagem', 'link_imagem')
    search_fields = ('latex_text', 'gabarito')
    ordering = ('disciplina', 'assunto')
    list_filter = ['assunto']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'assunto':
            # Check if we are editing an existing 'Questao' (so we have an instance)
            if hasattr(self, 'instance') and self.instance:
                disciplina_id = self.instance.disciplina_id
            else:
                # Try to retrieve 'disciplina' from the POST data (used during form submission)
                disciplina_id = request.POST.get('disciplina', None)

            # If we have a valid 'disciplina_id', filter the 'Assunto' queryset
            if disciplina_id:
                kwargs['queryset'] = Assunto.objects.filter(disciplina_id=disciplina_id)
            else:
                # No 'disciplina' selected yet, return an empty queryset
                kwargs['queryset'] = Assunto.objects.none()

        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def disciplina_nome(self, obj):
        return obj.disciplina.nome
    disciplina_nome.short_description = 'Disciplina'

    def assunto_nome(self, obj):
        return obj.assunto.nome
    assunto_nome.short_description = 'Assunto'

    def get_form(self, request, obj=None, **kwargs):
        # Store the current object instance for later use in formfield_for_foreignkey
        self.instance = obj
        return super().get_form(request, obj, **kwargs)



    
