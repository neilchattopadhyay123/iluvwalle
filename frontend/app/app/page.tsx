"use client"

import type React from "react"

import { useState } from "react"
import { Navigation } from "@/components/navigation"
import { Footer } from "@/components/Footer"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Camera, Upload, Recycle, AlertCircle, CheckCircle2, Info } from "lucide-react"

type RecyclingResult = {
  material: string
  category: string
  recyclable: boolean
  instructions: string[]
  preparation: string[]
  binType: string
}

export default function AppPage() {
  const [selectedImage, setSelectedImage] = useState<string | null>(null)
  const [isAnalyzing, setIsAnalyzing] = useState(false)
  const [result, setResult] = useState<RecyclingResult | null>(null)

  const handleImageUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]
    if (file) {
      const reader = new FileReader()
      reader.onloadend = () => {
        setSelectedImage(reader.result as string)
        analyzeImage()
      }
      reader.readAsDataURL(file)
    }
  }

  const analyzeImage = () => {
    setIsAnalyzing(true)
    setResult(null)

    // Simulate AI analysis
    setTimeout(() => {
      setResult({
        material: "Plastic Bottle (PET #1)",
        category: "Plastic",
        recyclable: true,
        instructions: [
          "Remove cap and place separately in recycling",
          "Empty all liquid contents",
          "Rinse bottle with water",
          "Crush bottle to save space",
          "Place in blue recycling bin",
        ],
        preparation: ["Remove labels if possible (optional)", "Ensure bottle is clean and dry"],
        binType: "Blue Recycling Bin",
      })
      setIsAnalyzing(false)
    }, 2000)
  }

  const handleReset = () => {
    setSelectedImage(null)
    setResult(null)
    setIsAnalyzing(false)
  }

  return (
    <div className="min-h-screen bg-background">
      <Navigation />

      <div className="bg-gradient-to-br from-primary/20 via-accent/10 to-secondary/20 border-b border-border">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8 py-12">
          <div className="max-w-4xl mx-auto">
            <div className="text-center">
              <h1 className="text-3xl sm:text-4xl font-bold mb-4">Sensor Dashboard</h1>
              <p className="text-muted-foreground">
                Scan any item to receive sorting instructions.
              </p>
            </div>
          </div>
        </div>
      </div>

      <div className="container mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="max-w-4xl mx-auto">
          <div className="grid lg:grid-cols-2 gap-8">
            {/* Upload Section */}
            <Card className="bg-card">
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <Camera className="h-5 w-5 text-primary" />
                  Current Item
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="space-y-4">
                    <div className="border-2 border-dashed border-border rounded-lg p-12 text-center hover:border-primary/50 transition-colors">
                      <p className="text-md text-muted-foreground mb-4">No items to be sorted</p>
                    </div>

                    <div className="flex items-start gap-2 text-sm text-muted-foreground bg-muted/50 p-4 rounded-lg">
                      <Info className="h-4 w-4 mt-0.5 flex-shrink-0" />
                      <p>
                        For best results, ensure the item is clearly visible and well-lit. Our AI works with bottles,
                        cans, paper, cardboard, and more.
                      </p>
                    </div>
                  </div>
              </CardContent>
            </Card>

            {/* Results Section */}
            <Card className="bg-card">
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <Recycle className="h-5 w-5 text-primary" />
                  Recycling Information
                </CardTitle>
              </CardHeader>
              <CardContent>
                {!result && !isAnalyzing && (
                  <div className="flex flex-col items-center justify-center py-12 text-center">
                    <AlertCircle className="h-12 w-12 text-muted-foreground mb-4" />
                    <p className="text-muted-foreground">Place item in front of sensor to see recycling instructions</p>
                  </div>
                )}

                {result && (
                  <div className="space-y-6">
                    <div>
                      <div className="flex items-start justify-between mb-2">
                        <h3 className="text-xl font-semibold">{result.material}</h3>
                        <Badge
                          variant={result.recyclable ? "default" : "destructive"}
                          className={result.recyclable ? "bg-primary" : ""}
                        >
                          {result.recyclable ? (
                            <CheckCircle2 className="h-3 w-3 mr-1" />
                          ) : (
                            <AlertCircle className="h-3 w-3 mr-1" />
                          )}
                          {result.recyclable ? "Recyclable" : "Not Recyclable"}
                        </Badge>
                      </div>
                      <p className="text-sm text-muted-foreground">Category: {result.category}</p>
                    </div>

                    <div className="bg-primary/5 border border-primary/20 rounded-lg p-4">
                      <div className="flex items-center gap-2 mb-2">
                        <div className="h-8 w-8 rounded-full bg-primary flex items-center justify-center">
                          <Recycle className="h-4 w-4 text-primary-foreground" />
                        </div>
                        <span className="font-semibold text-primary">{result.binType}</span>
                      </div>
                    </div>

                    <div>
                      <h4 className="font-semibold mb-3">Recycling Instructions:</h4>
                      <ol className="space-y-2">
                        {result.instructions.map((instruction, index) => (
                          <li key={index} className="flex gap-3">
                            <span className="flex-shrink-0 h-6 w-6 rounded-full bg-primary/10 text-primary flex items-center justify-center text-sm font-medium">
                              {index + 1}
                            </span>
                            <span className="text-sm text-muted-foreground leading-relaxed pt-0.5">{instruction}</span>
                          </li>
                        ))}
                      </ol>
                    </div>

                    <div>
                      <h4 className="font-semibold mb-3">Preparation Tips:</h4>
                      <ul className="space-y-2">
                        {result.preparation.map((tip, index) => (
                          <li key={index} className="flex gap-2 text-sm text-muted-foreground">
                            <CheckCircle2 className="h-4 w-4 text-primary flex-shrink-0 mt-0.5" />
                            <span className="leading-relaxed">{tip}</span>
                          </li>
                        ))}
                      </ul>
                    </div>
                  </div>
                )}
              </CardContent>
            </Card>
          </div>

          <Card className="mt-8 bg-gradient-to-br from-primary/5 via-accent/5 to-secondary/5 border-primary/20">
            <CardContent>
              <div className="flex items-start gap-3">
                <Info className="h-5 w-5 text-primary flex-shrink-0 mt-0.5" />
                <div className="space-y-2 text-sm text-muted-foreground">
                  <p className="font-medium text-foreground">Reminder:</p>
                  <ul className="space-y-1 list-disc list-inside">
                    <li>Sorting guidelines may vary by location</li>
                    <li>Always verify with your local waste management facility</li>
                    <li>When uncertain, ask for guidance—every correct sort matters</li>
                  </ul>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>
      </div>

      {/* Footer */}
      <Footer />
    </div>
  )
}
