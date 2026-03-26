"""Invoke tasks for online-cv."""

from invoke import Context, task


@task
def install(c: Context) -> None:
    """Install the required bundler version and gems."""
    c.run("gem install --user-install bundler:2.3.19")
    c.run("bundle config set --local path 'vendor/bundle'")
    c.run("bundle install")


@task
def serve(c: Context) -> None:
    """Start Jekyll locally with live reload. http://localhost:4000"""
    c.run("Open http://0.0.0.0:4000")
    c.run("bundle exec jekyll serve --livereload", pty=True)
