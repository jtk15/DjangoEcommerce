from django.db import models

class Category(models.Model):
    
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Idnetificaodr', max_length=100)
    
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']
    
    def __str__(self):
        
        return self.name


class Product(models.Model):
    
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    category = models.ForeignKey(Category, related_name='categories', verbose_name='categoria', on_delete=models.PROTECT)
    description = models.CharField('Descrição', max_length=200, blank=True)
    
    created = models.DateTimeField('Croado em', auto_now_add=True)
    modified = models.DateTimeField('Modifica em', auto_now=True)
    
    class Meta:
        
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['name']
        
    def __str__(self):
        
        return self.name
