#!/usr/bin/env python3
"""
Generate Ark-themed dinosaur icon using application colors
"""

from PIL import Image, ImageDraw
import os

def create_all_sizes():
    """Create dinosaur icon in multiple sizes using app colors"""
    
    # App colors
    bg_dark = (43, 43, 43)      # Dark background from app
    teal = (0, 191, 165)        # Teal accent from app
    teal_bright = (0, 255, 200) # Bright teal for highlights
    white = (255, 255, 255)     # White for details
    shadow = (0, 100, 80)       # Dark teal shadow
    
    icon_images = []
    
    # Create images for each size
    for size in [16, 32, 64, 128, 256]:
        img = Image.new('RGB', (size, size), bg_dark)
        draw = ImageDraw.Draw(img)
        
        cx = size / 2
        cy = size / 2
        
        # T-Rex style dinosaur in profile
        
        # BODY - large oval (teal)
        body_width = int(size * 0.45)
        body_height = int(size * 0.28)
        body_left = int(cx - body_width/2)
        body_top = int(cy - body_height/2)
        draw.ellipse(
            [body_left, body_top, body_left + body_width, body_top + body_height],
            fill=teal
        )
        
        # HEAD - larger circle in front (teal bright)
        head_radius = int(size * 0.16)
        head_x = int(cx + body_width/2.5)
        head_y = int(cy - size * 0.08)
        draw.ellipse(
            [head_x - head_radius, head_y - head_radius,
             head_x + head_radius, head_y + head_radius],
            fill=teal_bright
        )
        
        # SNOUT/JAW - extended pointed shape
        snout_width = int(size * 0.18)
        snout_height = int(size * 0.11)
        snout_x = head_x + head_radius - int(size * 0.03)
        snout_y = head_y
        
        # Draw snout as a kind of rectangle
        draw.polygon(
            [(snout_x, snout_y - snout_height//2),
             (snout_x + snout_width, snout_y),
             (snout_x, snout_y + snout_height//2),
             (snout_x - int(size * 0.05), snout_y)],
            fill=teal
        )
        
        # EYES - distinct white circles
        eye_radius = int(size * 0.055)
        eye_y = head_y - int(size * 0.07)
        left_eye_x = head_x - int(size * 0.08)
        
        draw.ellipse(
            [left_eye_x - eye_radius, eye_y - eye_radius,
             left_eye_x + eye_radius, eye_y + eye_radius],
            fill=white
        )
        
        # Pupil
        pupil_r = int(size * 0.025)
        draw.ellipse(
            [left_eye_x - pupil_r, eye_y - pupil_r,
             left_eye_x + pupil_r, eye_y + pupil_r],
            fill=shadow
        )
        
        # DORSAL SPIKES - prominently displayed on back
        spike_width = int(size * 0.05)
        spike_height = int(size * 0.16)
        spike_y_base = body_top - int(size * 0.01)
        
        # Spike 1 (front)
        spike1_x = body_left + int(size * 0.12)
        draw.polygon(
            [(spike1_x - spike_width, spike_y_base),
             (spike1_x, spike_y_base - spike_height),
             (spike1_x + spike_width, spike_y_base)],
            fill=teal_bright
        )
        
        # Spike 2 (middle) - taller
        spike2_x = body_left + int(size * 0.25)
        tall_spike = int(size * 0.2)
        draw.polygon(
            [(spike2_x - spike_width, spike_y_base),
             (spike2_x, spike_y_base - tall_spike),
             (spike2_x + spike_width, spike_y_base)],
            fill=teal_bright
        )
        
        # Spike 3 (back)
        spike3_x = body_left + int(size * 0.38)
        draw.polygon(
            [(spike3_x - spike_width, spike_y_base),
             (spike3_x, spike_y_base - spike_height),
             (spike3_x + spike_width, spike_y_base)],
            fill=teal_bright
        )
        
        # TAIL - long curved tail extending back
        tail_start_x = body_left
        tail_start_y = cy
        tail_end_x = body_left - int(size * 0.35)
        tail_end_y = tail_start_y - int(size * 0.15)
        
        # Draw tail as a thick curve
        for i in range(3):
            offset = i * int(size * 0.02)
            draw.line(
                [(tail_start_x - offset, tail_start_y + offset),
                 (tail_end_x, tail_end_y)],
                fill=teal, width=max(2, int(size * 0.05))
            )
        
        # LEGS - two thick back legs
        leg_width = int(size * 0.06)
        leg_height = int(size * 0.2)
        body_bottom = body_top + body_height
        
        # Back leg 1
        leg1_x = body_left + int(size * 0.15)
        draw.rectangle(
            [leg1_x - leg_width//2, body_bottom,
             leg1_x + leg_width//2, body_bottom + leg_height],
            fill=teal
        )
        
        # Back leg 2
        leg2_x = body_left + int(size * 0.35)
        draw.rectangle(
            [leg2_x - leg_width//2, body_bottom,
             leg2_x + leg_width//2, body_bottom + leg_height],
            fill=teal
        )
        
        # Small arm/claw at head
        arm_x = head_x - int(size * 0.1)
        arm_y = head_y + int(size * 0.08)
        claw_size = int(size * 0.03)
        draw.polygon(
            [(arm_x, arm_y),
             (arm_x - claw_size, arm_y + claw_size),
             (arm_x + claw_size, arm_y + claw_size)],
            fill=teal_bright
        )
        
        # NOSTRIL on snout
        nostril_x = snout_x + int(size * 0.08)
        nostril_y = snout_y - int(size * 0.02)
        nostril_size = max(1, int(size * 0.02))
        draw.ellipse(
            [nostril_x - nostril_size, nostril_y - nostril_size,
             nostril_x + nostril_size, nostril_y + nostril_size],
            fill=shadow
        )
        
        icon_images.append(img)
    
    # Save as proper multi-resolution ICO
    output_path = "source/icon.ico"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Save with all sizes
    icon_images[0].save(
        output_path,
        format='ICO',
        sizes=[(16, 16), (32, 32), (64, 64), (128, 128), (256, 256)],
        append_images=icon_images[1:]
    )
    
    print(f"✅ T-Rex dinosaur icon created: {output_path}")

if __name__ == "__main__":
    create_all_sizes()
