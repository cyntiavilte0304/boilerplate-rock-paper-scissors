# Solución avanzada para ganar a los 4 bots de freeCodeCamp
# detecta patrones, ajusta contra cada bot y cambia de táctica si es necesario.

def player(prev_play, opponent_history=[]):
    # Guardamos la jugada previa del oponente
    if prev_play:
        opponent_history.append(prev_play)

    # Movimientos que vencen a otros movimientos
    counter = {"R": "P", "P": "S", "S": "R"}

    # --- Estrategia 1: si no tenemos historial suficiente, jugamos "P"
    if len(opponent_history) < 3:
        return "P"

    # --- Estrategia 2: detectar patrones cortos repetidos (n-grams)
    pattern_length = 3
    if len(opponent_history) > pattern_length:
        recent = opponent_history[-pattern_length:]
        
        # Buscamos este patrón en el historial, excepto al final
        for i in range(len(opponent_history)-pattern_length-1):
            if opponent_history[i:i+pattern_length] == recent:
                predicted = opponent_history[i + pattern_length]
                return counter[predicted]  # Contraataque

    # --- Estrategia 3: detectar si el bot usa ciclos (como Abby o Mrugesh)
    counts = {"R": 0, "P": 0, "S": 0}
    for move in opponent_history:
        if move in counts:
            counts[move] += 1

    # El movimiento más común del oponente
    most_common = max(counts, key=counts.get)

    # Respondemos con lo que vence al movimiento más común
    return counter[most_common]

