import Link from "next/link"
import { Navigation } from "@/components/navigation"
import { Footer } from "@/components/Footer"
import { Button } from "@/components/ui/button"
import { Play, Info, Camera, Recycle, Leaf } from "lucide-react"

export default function HomePage() {
  return (
    <div className="min-h-screen bg-background">
      <Navigation />

      {/* Hero Banner Section - Disney+ Style */}
      <section className="relative h-[70vh] lg:h-[85vh] overflow-hidden">
        <div className="absolute inset-0">
          <img src="/walle-space-background.webp" alt="WALL-E in space" className="w-full h-full object-cover" />
          <div className="absolute inset-0 bg-gradient-to-t from-background via-background/40 to-transparent" />
          <div className="absolute inset-0 bg-gradient-to-r from-background/60 via-transparent to-transparent" />
        </div>

        <div className="relative container mx-auto px-4 sm:px-6 lg:px-8 h-full flex items-end pb-16 lg:pb-24">
          <div className="max-w-2xl space-y-6">
            <div className="space-y-2">
              <h1 className="text-5xl sm:text-6xl lg:text-7xl font-bold text-balance leading-tight text-foreground">
                I Luv WALL-E
              </h1>
            </div>

            <p className="text-lg lg:text-xl text-foreground/90 leading-relaxed max-w-xl">
              After hundreds of years of waste, discover a new purpose with our AI-powered recycling identification
              system. Join WALL-E's mission to clean up Earth, one item at a time.
            </p>

            <div className="flex flex-wrap gap-3">
              <Button asChild size="lg" className="bg-primary text-primary-foreground hover:bg-primary/90 gap-2">
                <Link href="/app">
                  <Play className="h-5 w-5 fill-current" />
                  Start Scanning
                </Link>
              </Button>
              <Button asChild size="lg" variant="secondary" className="gap-2">
                <Link href="/about">
                  <Info className="h-5 w-5" />
                  Learn More
                </Link>
              </Button>
            </div>
          </div>
        </div>
      </section>

      {/* Details Section - Disney+ Style */}
      <section className="py-12 lg:py-16">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8">
          <div className="max-w-4xl">
            <h2 className="text-3xl sm:text-4xl font-bold mb-6">Details</h2>

            <div className="space-y-6">
              <p className="text-lg text-muted-foreground leading-relaxed">
                Travel to a future not so far away for an environmental mission about a determined recycling program
                named after WALL-E. After hundreds of years of waste accumulation, discover a new purpose with our
                curious and lovable AI system that helps identify and sort recyclables correctly. Join us on a fantastic
                journey to restore our planet.
              </p>

              <div className="grid sm:grid-cols-2 gap-6 text-sm">
                <div>
                  <div className="text-muted-foreground mb-1">Technology</div>
                  <div className="font-medium">AI-Powered Recognition</div>
                </div>
                <div>
                  <div className="text-muted-foreground mb-1">Accuracy</div>
                  <div className="font-medium">98% Identification Rate</div>
                </div>
                <div>
                  <div className="text-muted-foreground mb-1">Mission</div>
                  <div className="font-medium">Environmental Restoration</div>
                </div>
                <div>
                  <div className="text-muted-foreground mb-1">Users</div>
                  <div className="font-medium">Neil, Brandon, Nick, Imad, HackPSU Judges</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section - "You May Also Like" Style */}
      <section className="py-12 lg:py-16 bg-muted/20">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-2xl sm:text-3xl font-bold mb-8">How It Works</h2>

          <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
            <div className="group cursor-pointer">
              <div className="aspect-video bg-gradient-to-br from-primary/20 to-primary/5 rounded-lg mb-4 flex items-center justify-center border border-border hover:border-primary/50 transition-all">
                <Camera className="h-16 w-16 text-primary" />
              </div>
              <h3 className="text-xl font-semibold mb-2">Scan</h3>
              <p className="text-sm text-muted-foreground leading-relaxed">
                Capture any item with your camera. From bottles to boxes, we'll identify it all instantly.
              </p>
            </div>

            <div className="group cursor-pointer">
              <div className="aspect-video bg-gradient-to-br from-secondary/20 to-secondary/5 rounded-lg mb-4 flex items-center justify-center border border-border hover:border-secondary/50 transition-all">
                <Recycle className="h-16 w-16 text-secondary" />
              </div>
              <h3 className="text-xl font-semibold mb-2">Analyze</h3>
              <p className="text-sm text-muted-foreground leading-relaxed">
                Our AI system instantly identifies the material and tells you exactly what to do with it.
              </p>
            </div>

            <div className="group cursor-pointer">
              <div className="aspect-video bg-gradient-to-br from-accent/20 to-accent/5 rounded-lg mb-4 flex items-center justify-center border border-border hover:border-accent/50 transition-all">
                <Leaf className="h-16 w-16 text-accent" />
              </div>
              <h3 className="text-xl font-semibold mb-2">Restore</h3>
              <p className="text-sm text-muted-foreground leading-relaxed">
                Follow the instructions and help give materials a second life. Every action counts toward Earth's
                restoration.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <Footer />
    </div>
  )
}
