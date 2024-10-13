from browser import document, html, window
import math

# Create canvas and context
canvas = html.CANVAS(width=600, height=600)
document <= canvas
ctx = canvas.getContext("2d")

def draw_heart(scale, color):
    ctx.clearRect(0, 0, canvas.width, canvas.height)  # Clear canvas
    ctx.beginPath()
    ctx.strokeStyle = color
    ctx.lineWidth = 5
    ctx.translate(300, 300)  # Center the heart

    # Parametric heart equation
    for t in range(0, 360):
        rad = math.radians(t)
        x = 16 * math.sin(rad) ** 3 * scale
        y = -(13 * math.cos(rad) - 5 * math.cos(2 * rad) - 2 * math.cos(3 * rad) - math.cos(4 * rad)) * scale
        if t == 0:
            ctx.moveTo(x, y)
        else:
            ctx.lineTo(x, y)

    ctx.stroke()
    ctx.resetTransform()  # Reset canvas translation

# Animation variables
frame = 0

def animate(timestamp):
    global frame
    scale = 1 + 0.2 * math.sin(frame / 10)  # Smooth pulse
    red = (math.sin(frame / 10) + 1) / 2  # Red component (0 to 1)
    blue = (math.cos(frame / 15) + 1) / 2  # Blue component (0 to 1)
    color = f"rgb({int(255 * red)}, 0, {int(255 * blue)})"  # Dynamic color

    draw_heart(scale, color)
    frame += 1
    window.requestAnimationFrame(animate)

# Start animation
window.requestAnimationFrame(animate)
