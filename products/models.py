from django.db import models

# Create your models here.
class ProductMaster(models.Model):
	enum_choices = (
		('y', 'y'),
		('n', 'n')
	)
	exclusive = (
		('y', 'y'),
		('n', 'n'),
		('o', 'o'),
	)
	#Basic Product Fields
	name = models.CharField(max_length=255,blank=True, null=True)
	sku = models.CharField(max_length=255, blank=True, null=True)
	title = models.CharField(max_length=255, blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	visibility = models.BooleanField(default=False)
	status = models.CharField(max_length=255,blank=True, null=True)
	weight = models.FloatField(blank=True, null=True)
	width = models.FloatField(blank=True, null=True)
	depth  = models.FloatField(blank=True, null=True)
	height = models.FloatField(blank=True, null=True)
	isbn = models.TextField(blank=True, null=True)
	asin = models.TextField(blank=True, null=True)
	slug = models.TextField(blank=True, null=True)
	old_slug = models.TextField(blank=True, null=True)
	uom = models.CharField(max_length=255, blank=True, null=True)
	warranty = models.CharField(max_length=255, blank=True, null=True)
	search_keywords = models.TextField(blank=True, null=True)
	installation_required = models.CharField(max_length=2,choices=enum_choices,default='n')
	is_customised = models.CharField(max_length=2,choices=enum_choices,default='n')
	product_type = models.CharField(max_length=255, null=True, blank=True)
	hsn_id = models.TextField(blank=True, null=True)
	is_featured = models.BooleanField(default=False)
	is_auctionable = models.IntegerField(blank=True, null=True)
	#Time stamps
	created_at = models.DateField(auto_now=True)
	updated_at = models.DateField(auto_now_add=True)
	#Preorder Product settings
	preorder_release_date = models.CharField(max_length=255, blank=True, null=True)
	preorder_message = models.TextField(blank=True, null=True)
	is_preorder_only = models.BooleanField(default=False)
	#Search Engine Optimization	
	meta_url = models.CharField(max_length=255, blank=True, null=True)
	meta_title = models.CharField(max_length=255, blank=True, null=True)
	meta_key_word = models.TextField(blank=True, null=True)
	meta_description = models.TextField(blank=True, null=True)
	url = models.CharField(max_length=255, blank=True, null=True)
	#Additional	
	max_order_unit = models.CharField(max_length=255, blank=True, null=True)
	brand = models.CharField(max_length=255, blank=True, null=True)
	last_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
	avg_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
	default_price = models.FloatField(blank=True, null=True)
	cost_per_unit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
	quantity = models.IntegerField(blank=True, null=True)	
	numberof_sale = models.IntegerField(default=0,blank=True, null=True)
	numberof_view = models.IntegerField(default=0,blank=True, null=True)	
	sla = models.IntegerField(blank=True, null=True)
	product_offer_start_date = models.DateField(blank=True, null=True)
	product_offer_end_date = models.DateField(blank=True, null=True)
	ip_address = models.CharField(max_length=255, blank=True, null=True)	
	minimum_inventory=models.CharField(max_length=250, blank=True, null=True)
	maximum_inventory=models.CharField(max_length=250, blank=True, null=True)
	desired_inventory=models.CharField(max_length=250, blank=True, null=True)
	selling_loose=models.CharField(max_length=10, default='n', blank=True, null=True)
	selling_rule=models.CharField(max_length=250, blank=True, null=True)
	mode_of_delivery = models.CharField(max_length=50, blank=True, null=True)

	class Meta:
		db_table = 'product_master'

class CategoryMasters(models.Model):
	enum_choices = (
		('y', 'y'),
		('n', 'n')
	)
	status_choices = (
		('Y', 'Y'),
		('N', 'N')
	)
	name = models.CharField(max_length=255,blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	parent_id = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
	display_order = models.IntegerField(blank=True, null=True)
	image = models.CharField(max_length=255, blank=True, null=True)
	thumb_image = models.CharField(max_length=255, blank=True, null=True)
	page_title = models.CharField(max_length=255, blank=True, null=True)
	category_url = models.CharField(max_length=255, blank=True, null=True)
	slug = models.TextField(blank=True, null=True)
	createdby = models.IntegerField(blank=True, null=True)
	updatedby = models.IntegerField(blank=True, null=True)
	isdeleted = models.CharField(max_length=2,choices=enum_choices,default='n', blank=True, null=True)
	isblocked = models.CharField(max_length=2,choices=enum_choices,default='n', blank=True, null=True)
	customer_group_id = models.IntegerField(blank=True, null=True)
	display_mobile_app = models.CharField(max_length=2,choices=status_choices,default='N', blank=True, null=True)
	applicable_imei = models.CharField(max_length=2,choices=status_choices,default='N',blank=True, null=True)
	category_collection = models.CharField(max_length=2,choices=enum_choices,default='n', blank=True, null=True)
	category_type = models.CharField(max_length=50,blank=True, null=True)

	class Meta:
		db_table = 'category_masters'