from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
class Spell(models.Model):
    ATTACK_TYPE = [
        ('MELEE', 'Melee spell attack'),
        ('RANGED', 'Ranged spell attack')
    ]

    COMPONENTS = [
        ('V', 'Verbal'),
        ('S', 'Somatic'),
        ('M', 'Material')
    ]

    SPELL_LEVEL = [
        (0, 'cantrip'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9')
    ]

    SCHOOL = [
        ('ABJURATION', 'Abjuration'),
        ('CONJURATION', 'Conjuration'),
        ('DIVINATION', 'Divination'),
        ('ENCHANTMENT', 'Enchantment'),
        ('EVOCATION', 'Evocation'),
        ('ILLUSION', 'Illusion'),
        ('NECROMANCY', 'Necromancy'),
        ('TRANSMUTATION', 'Transmutation')
    ]

    CLASSES = [
    # commenting out classes with no spells, may make class model later
    #    ('BARBARIAN', 'Barbarian'),
        ('BARD', 'Bard'),
        ('CLERIC', 'Cleric'),
        ('DRUID', 'Druid'),
    #    ('FIGHTER', 'Fighter'),
    #    ('MONK', 'Monk'),
        ('PALADIN', 'Paladin'),
        ('RANGER', 'Ranger'),
    #    ('ROGUE', 'Rogue'),
        ('SORCEROR', 'Sorceror'),
        ('WARLOCK', 'Warlock'),
        ('WIZARD', 'Wizard')
    ]

    CONDITIONS = [
        ('BLINDED', 'Blinded'),
        ('CHARMED', 'Charmed'),
        ('DEAFENED', 'Deafened'),
        ('FRIGHTENED', 'Frightened'),
        ('GRAPPLED', 'Grappled'),
        ('INCAPACITATED', 'Incapacitated'),
        ('INVISIBLE', 'Invisible'),
        ('PARALYZED', 'Paralyzed'),
        ('PETRIFIED', 'Petrified'),
        ('POISONED', 'Poisoned'),
        ('PRONE', 'Prone'),
        ('RESTRAINED', 'Restrained'),
        ('STUNNED', 'Stunned'),
        ('UNCONSCIOUS', 'Unconscious')
    ]

    DAMAGE_TYPE = [
        ('ACID', 'Acid'),
        ('BLUDGEONING', 'Bludgeoning'),
        ('COLD', 'Cold'),
        ('FIRE', 'Fire'),
        ('FORCE', 'Force'),
        ('LIGHTNING', 'Lightning'),
        ('NECROTIC', 'Necrotic'),
        ('PIERCING', 'Piercing'),
        ('POISON', 'Poison'),
        ('PSYCHIC', 'Psychic'),
        ('RADIANT', 'Radiant'),
        ('SLASHING', 'Slashing'),
        ('THUNDER', 'Thunder')
    ]

    name = models.CharField('spell name', max_length=100, unique=True)
    desc = models.TextField('description')
    higher_level = models.TextField(blank=True)
    attack_type = models.CharField(choices=ATTACK_TYPE, max_length=6, blank=True)
    spell_range = models.CharField(max_length=50)
    area = models.CharField('area of effect', max_length=50, blank=True)
    components = MultiSelectField(choices=COMPONENTS, max_choices=3, max_length=3)
    materials = models.CharField(max_length=500, blank=True)
    ritual = models.BooleanField()
    duration = models.CharField('spell duration', max_length=100)
    concentration = models.BooleanField()
    casting_time = models.CharField(max_length=100)
    level = models.IntegerField(verbose_name='spell level', choices=SPELL_LEVEL)
    school = models.CharField('school of magic', max_length=20, choices=SCHOOL)
    character_classes = MultiSelectField(choices=CLASSES, max_choices=8, default='WIZARD')
    character_subclasses = models.CharField(max_length=200, blank=True)
    conditions = MultiSelectField(choices=CONDITIONS, max_choices=14, blank=True)
    damage_types = MultiSelectField(choices=DAMAGE_TYPE, max_choices=13, blank=True)
