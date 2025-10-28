def take_magic_damage(health, resist, amp, spell_power):
    total_max_damage = spell_power * amp - resist
    new_health = health - total_max_damage
    return new_health

