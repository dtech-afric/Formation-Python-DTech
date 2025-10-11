def with_timer(duration: int):
    """
    Décorateur pour imposer un timer sur une fonction.
    Si le joueur ne répond pas dans 'duration' secondes,
    on considère la question comme ratée.
    """
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            # Démarrer un compte à rebours
            self.time_left = duration
            self.update_timer_label()

            # planifier une action automatique quand le temps est écoulé
            self.after(duration * 1000, lambda: self._time_expired(func))
            
            return func(self, *args, **kwargs)
        return wrapper
    return decorator
